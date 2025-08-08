from flask import Flask, render_template, request, session, redirect
from flask.views import MethodView
from game.game_engine import GameEngine
from models import db, User, QuestionSet, Question, GameResult

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.secret_key = "dev.secret"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/debug-session')
def debug_session():
    """Returns the current session data for debugging purposes."""
    return dict(session)

@app.route('/clear-session')
def clear_session():
    """Clears all session data and returns the now-empty session dictionary."""
    session.clear()
    return dict(session)

@app.route('/')
def home():
    """Renders the homepage (index.html)."""
    return render_template("index.html")

@app.route('/scoreboard')
def scoreboard():
    """
    Displays the scoreboard by querying all GameResult entries 
    and sorting them in descending order by score.
    """
    games = GameResult.query.order_by(GameResult.score.desc()).all()
    return render_template("scoreboard.html", games=games)

@app.route('/enter-name', methods=['GET', 'POST'])
def enter_name():
    """
    Handles player name input and game mode selection.

    On POST:
    - Checks if the user exists by username; creates one if not.
    - Saves user data to the session.
    - Redirects to either the default game or custom set chooser based on selection.
    
    On GET:
    - Renders the enter_name.html form.
    """
    if request.method == 'POST':
        player_name = request.form['player_name']
        game_type = request.form['game_type']

        user = User.query.filter_by(username=player_name).first()
        if not user:
            user = User(username=player_name)
            db.session.add(user)
            db.session.commit()

        session['player_name'] = user.username
        session['user_id'] = user.id

        if game_type == 'default':
            return redirect('/start')
        elif game_type == 'custom':
            return redirect('/custom-sets')

    return render_template('enter_name.html')

def save_game_result(player_score, set_title="Default"):
    """
    Saves a player's GameResult to the database.

    If the QuestionSet with the given title doesn't exist, creates it.
    Associates the result with the current user and the correct set.
    
    Returns:
        The QuestionSet instance used for the result.
    """
    user_id = session.get('user_id', 1)
    question_set = QuestionSet.query.filter_by(title=set_title).first()

    if not question_set:
        question_set = QuestionSet(title=set_title, creator_id=user_id)
        db.session.add(question_set)
        db.session.commit()

    game_result = GameResult(
        user_id=user_id,
        set_id=question_set.id,
        score=player_score
    )
    db.session.add(game_result)
    db.session.commit()

    return question_set

@app.route('/start', methods=['GET', 'POST'])
def display_question():
    """
    Handles the default quiz gameplay loop using questions from a JSON source.

    On GET:
    - Initializes a new game round.

    On POST:
    - Processes the user's selected answer.
    - Provides feedback.
    - Tracks and increments score and question index.

    When questions are exhausted:
    - Saves the game result.
    - Renders the results screen.
    """
    session.pop('current_custom_set', None)
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
        if selected and question.is_correct(selected):
            feedback = {"correct": True, "message": "Correct!"}
            player_score += 1
        else:
            feedback = {"correct": False, "message": "Wrong!"}
        current_question += 1
        engine.current_index = current_question

    if engine.has_more_questions():
        question = engine.get_current_question()
    else:
        set_title = session.get('current_custom_set', 'Default')
        save_game_result(player_score, set_title)

        local_scores = session.get('local_scores', [])
        local_scores.append({
            "player": session.get('player_name', 'Anonymous'),
            "score": player_score,
            "game": set_title
        })
        session['local_scores'] = local_scores

        return render_template("results.html", player_score=player_score)

    return render_template(
        "game_question.html",
        question=question,
        feedback=feedback,
        player_score=player_score,
        current_question=current_question,
    )

@app.route('/custom', methods=['GET', 'POST'])
def custom_game():
    """
    Allows players to build and save a custom question set.

    On GET:
    - Renders the custom_game.html form.
    - If reset=true is passed, clears the current custom set.

    On POST:
    - First step: captures the custom set name.
    - Second step: collects individual questions and adds them to session.
    """
    if request.args.get('reset') == 'true':
        session.pop('custom_set_name', None)
        session.pop('custom_questions', None)
        return render_template('index.html', success=False)

    if request.method == 'POST':
        if 'set_name' in request.form:
            session['custom_set_name'] = request.form['set_name']
            session['custom_questions'] = []
            return render_template('custom_game.html', success=False)

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

@app.route('/custom-game-play', methods=['GET', 'POST'])
def custom_game_play():
    """
    Plays through a custom question set saved in the session.

    On GET:
    - Renders the current question if available.

    On POST:
    - Checks the selected answer.
    - Updates score and index.
    - Saves GameResult at the end of the set.
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
            set_title = session.get('current_custom_set', 'Default')
            save_game_result(score, set_title)

            local_scores = session.get('local_scores', [])
            local_scores.append({
                "player": session.get('player_name', 'Anonymous'),
                "score": score,
                "game": set_title
            })
            session['local_scores'] = local_scores

            return render_template('results.html', player_score=score)

        current_question = questions[index]

    return render_template(
        "game_question.html",
        question=current_question,
        feedback=feedback,
        player_score=score,
        current_question=index,
    )

@app.route('/start-custom', methods=['POST'])
def start_custom():
    """
    Begins gameplay for a selected custom question set.

    Looks up the chosen set by name from session and loads it into 
    gameplay state. Then redirects to the /custom-game-play route.
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
    Displays a dropdown menu of available custom question sets 
    saved in the session. Renders choose_custom_set.html.
    """
    sets = session.get('all_custom_sets', {})
    return render_template('choose_custom_set.html', sets=sets.keys())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
