from flask import Flask, render_template, request, session, redirect
from flask.views import MethodView
from game.game_engine import GameEngine
from models import db, User, QuestionSet, Question, GameResult


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'  # Moved above init_app
app.secret_key = "dev.secret"  # Needed for session storage

db.init_app(app)

with app.app_context():
    db.create_all()

@app.before_request
def require_player_name():
    # List of routes to exclude from the check (and static files)
    exempt_routes = ['enter_name', 'static']

    # Skip check for exempt routes and static files
    if request.endpoint in exempt_routes or request.endpoint is None:
        return

    # Redirect to /enter-name if 'player_name' not in session
    if 'player_name' not in session:
        session['next'] = request.path  # Save where the user was going
        return redirect('/enter-name')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/scoreboard')
def scoreboard():
    games = GameResult.query.order_by(GameResult.score.desc()).all()
    print(games)
    return render_template("scoreboard.html", games=games)


@app.route('/enter-name', methods=['GET', 'POST'])
def enter_name():
    if request.method == 'POST':
        session['player_name'] = request.form['player_name']
        game_type = request.form['game_type']
        #look up if a user with this name exists, if not create one
        user = User.query.filter_by(username=session['player_name']).first()
        if not user:
            user = User(username=session['player_name'])
            db.session.add(user)
            db.session.commit()

        if game_type == 'default':
            return redirect('/start')
        elif game_type == 'custom':
            return redirect('/custom-sets')
        
    return render_template('enter_name.html')


@app.route('/start', methods=['GET', 'POST'])
def display_question():
    """
    Handles the main quiz gameplay route.
    
    On GET: Initializes a new game round by creating a GameEngine instance, 
    loading all questions from the JSON repository, resetting the game state 
    (score = 0, question index = 0), and fetching the first question.

    On POST: Processes the submitted answer by reading the selected option 
    from the form, checking its correctness using Question.is_correct(), 
    and updating the score and question index accordingly. Provides feedback 
    ("Correct!" or "Wrong!") for display.

    After processing, the route checks if more questions remain using 
    engine.has_more_questions(). If so, it renders the next question via 
    start.html. If not, it renders the final results via results.html.
    """

    session.pop('current_custom_set', None) # clear any leftover custom set name from previous games
    feedback = None
    player_score = int(request.form.get("current_score", 0))
    current_question = int(request.form.get("current_question", 0))

    engine = GameEngine()
    engine.load_questions_json()
    engine.current_index = current_question
    engine.score = player_score
    question = engine.get_current_question()

    if request.method == 'POST':
        selected = int(request.form.get("answer"))

        print(question.is_correct(selected))
        
        if selected and question.is_correct(selected):
            feedback = { "correct": True, "message": "Correct!" }
            player_score += 1
        else:
            feedback = { "correct": False, "message": "Wrong!" }
        current_question += 1
        engine.current_index = current_question
    
    if engine.has_more_questions():
        question = engine.get_current_question()
    else:
        # Stores score in memory before rendering results.html
        db.session.add(GameResult(
            user_id=session.get('user_id', 1),  # Default to user_id 1 if not set
            set_id=1,  # Default set_id, adjust as needed
            score=player_score
        ))
        db.session.commit()
        local_scores = session.get('local_scores', [])
        local_scores.append({
            "player": session.get('player_name', 'Anonymous'),
            "score": player_score,
            "game": session.get('current_custom_set', 'Default')
        })
        session['local_scores'] = local_scores

        return render_template("results.html", player_score=player_score)

    return render_template(
        "start.html",
        question=question,
        feedback=feedback,
        player_score=player_score,
        current_question=current_question,
    )




@app.route('/custom', methods=['GET', 'POST'])
def custom_game():
    """
    Manages the creation of custom question sets via a form, using session storage.

    On GET: Renders the custom_game.html page. If the query parameter `reset=true` is present, 
    the route clears any in-progress custom set from the session (removes 'custom_set_name' 
    and 'custom_questions') to start fresh. Otherwise, it simply displays the form.

    On POST:
    If the form includes a `set_name` field, it indicates the start of a new custom set. 
    The route stores the set name in the session, initializes an empty list for questions, 
    and re-renders the form with success=False.
    If the form includes question fields but no `set_name`, it processes a new question submission. 
    A dictionary containing the question prompt, options, and correct answer index is created 
    and appended to the session's 'custom_questions' list. This list is also saved under the 
    session's 'all_custom_sets' dictionary, keyed by the set name.

    After handling the submission, the form is re-rendered with a success flag to show confirmation, 
    allowing the user to add more questions.
    """

    if request.args.get('reset') == 'true':
        session.pop('custom_set_name', None)
        session.pop('custom_questions', None)
        return render_template('index.html', success=False)

    if request.method == 'POST':
        # name the set if not done yet
        if 'set_name' in request.form:
            session['custom_set_name'] = request.form['set_name']
            session['custom_questions'] = []  # Initialize fresh list
            return render_template('custom_game.html', success=False)
        
        # add a question
        q = {
            "category": "Custom",
            "prompt": request.form['prompt'],
            "options": [
                request.form['option_a'],
                request.form['option_b'],
                request.form['option_c'],
                request.form['option_d']
            ],
            "answer": int(request.form['correct'])
        }

        custom_qs = session.get('custom_questions', [])
        custom_qs.append(q)
        session['custom_questions'] = custom_qs

        custom_sets = session.get('all_custom_sets', {})
        set_name = session['custom_set_name']
        custom_sets[set_name] = custom_qs
        session['all_custom_sets'] = custom_sets

        return render_template('custom_game.html', success=True)

    return render_template('custom_game.html', success=False)

@app.route('/results')
def results():
    return render_template("results.html", player_score=0)

@app.route('/custom-game-play', methods=['GET', 'POST'])
def custom_game_play():
    """
    Implements the gameplay loop for a custom question set, similar to the /start route for the default game.

    On each request, retrieves the current question list, index, and score from the session.

    On GET: If there are questions remaining, renders the current question using the shared start.html template.
    On POST: Compares the submitted answer index directly to the stored correct answer index from the current question 
    (a plain dictionary from the session). Updates the score and index accordingly, and prepares a feedback message 
    ("Correct!" or "Wrong!"). Then:
        If all questions have been answered, renders the results.html page with the final score.
        Otherwise, renders the next question via start.html with updated feedback and score.

    This loop continues until all questions in the custom set have been completed.
    """

    questions = session.get('custom_game_questions', [])
    index = session.get('custom_current_index', 0)
    score = session.get('custom_score', 0)

    if index >= len(questions):
        return render_template('results.html', player_score=score)

    current_question = questions[index]
    feedback = None

    if request.method == 'POST':
        selected = int(request.form.get("answer", -1))
        if selected == current_question['answer']:
            feedback = {"correct": True, "message": "Correct!"}
            score += 1
        else:
            feedback = {"correct": False, "message": "Wrong!"}

        index += 1
        session['custom_current_index'] = index
        session['custom_score'] = score

        if index >= len(questions):
            # Stores score in memory before rendering results.html
            local_scores = session.get('local_scores', [])
            local_scores.append({
                "player": session.get('player_name', 'Anonymous'),
                "score": score,
                "game": session.get('current_custom_set', 'Default')
            })
            session['local_scores'] = local_scores
            return render_template('results.html', player_score=score)
        
        current_question = questions[index]

    return render_template(
        "start.html",
        question=current_question,
        feedback=feedback,
        player_score=score,
        current_question=index,
    )

# @app.route('/scoreboard')
# def scoreboard():
#     games = session.get('local_scores', [])
#     return render_template("scoreboard.html", games=games)

#     #games = GameResult.query.order_by(GameResult.score.desc()).all()
#     #print(games)

@app.route('/start-custom', methods=['POST'])
def start_custom():
    """
    Handles submission of the selected custom question set (via POST).

    Looks up the chosen set name from the form in session['all_custom_sets'] and retrieves 
    the corresponding list of questions. Initializes gameplay state in the session by setting 
    the selected set name, loading the questions into 'custom_game_questions', and resetting 
    'custom_current_index' and 'custom_score' to 0.

    Finally, redirects the user to the /custom-game-play route to begin the quiz.
    """

    set_name = request.form['set_choice']
    sets = session.get('all_custom_sets', {})
    questions = sets.get(set_name)

    if not questions:
        return "Set not found or empty", 400

    session['current_custom_set'] = set_name
    session['custom_game_questions'] = questions
    session['custom_current_index'] = 0
    session['custom_score'] = 0

    return redirect('/custom-game-play')

@app.route('/custom-sets', methods=['GET'])
def custom_sets():
    """
    Presents a page (choose_custom_set.html) where the user can select one of the saved custom 
    question sets to play.

    Retrieves the keys from session['all_custom_sets'] (the names of saved sets) 
    and passes them to the template to populate a dropdown menu. If no custom sets are found, 
    the template displays a message indicating that no sets are currently available.
    """
    
    sets = session.get('all_custom_sets', {})
    return render_template('choose_custom_set.html', sets=sets.keys())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
