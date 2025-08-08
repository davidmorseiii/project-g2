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
    session.clear()  # Remove all session variables
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
    games = GameResult.query.order_by(GameResult.score.desc()).all()  # Get all game results, highest score first
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
        player_name = request.form['player_name']  # Get player name from form
        game_type = request.form['game_type']      # Get selected game type

        user = User.query.filter_by(username=player_name).first()  # Look up user in DB
        if not user:
            user = User(username=player_name)  # Create new user if not found
            db.session.add(user)
            db.session.commit()

        session['player_name'] = user.username  # Store username in session
        session['user_id'] = user.id            # Store user id in session

        if game_type == 'default':
            return redirect('/start')           # Start default game
        elif game_type == 'custom':
            return redirect('/custom-sets')     # Go to custom set chooser

    # Render the name entry form
    return render_template('enter_name.html')

def save_game_result(player_score, set_title="Default"):
    """
    Saves a player's GameResult to the database.

    If the QuestionSet with the given title doesn't exist, creates it.
    Associates the result with the current user and the correct set.
    
    Returns:
        The QuestionSet instance used for the result.
    """
    user_id = session.get('user_id', 1)  # Get user id from session (default to 1)
    question_set = QuestionSet.query.filter_by(title=set_title).first()  # Find set by title

    if not question_set:
        question_set = QuestionSet(title=set_title, creator_id=user_id)  # Create set if not found
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
    session.pop('current_custom_set', None)  # Remove any custom set from session
    feedback = None
    player_score = int(request.form.get("current_score", 0))      # Current score from form or 0
    current_question = int(request.form.get("current_question", 0))  # Current question index from form or 0

    engine = GameEngine()                # Create game engine
    engine.load_questions_json()         # Load questions from JSON
    engine.current_index = current_question
    engine.score = player_score
    question = engine.get_current_question()  # Get the current question

    if request.method == 'POST':
        selected = int(request.form.get("answer"))  # Get selected answer
        if selected and question.is_correct(selected):
            feedback = {"correct": True, "message": "Correct!"}
            player_score += 1
        else:
            feedback = {"correct": False, "message": "Wrong!"}
        current_question += 1
        engine.current_index = current_question

    if engine.has_more_questions():
        question = engine.get_current_question()  # Next question
    else:
        set_title = session.get('current_custom_set', 'Default')
        save_game_result(player_score, set_title)  # Save result

        local_scores = session.get('local_scores', [])
        local_scores.append({
            "player": session.get('player_name', 'Anonymous'),
            "score": player_score,
            "game": set_title
        })
        session['local_scores'] = local_scores

        return render_template("results.html", player_score=player_score)

    # Render the question page
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
            session['custom_set_name'] = request.form['set_name']  # Store set name
            session['custom_questions'] = []                      # Start with empty question list
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
        custom_qs.append(q)  # Add new question to list
        session['custom_questions'] = custom_qs

        custom_sets = session.get('all_custom_sets', {})
        set_name = session['custom_set_name']
        custom_sets[set_name] = custom_qs  # Save set in session
        session['all_custom_sets'] = custom_sets

        return render_template('custom_game.html', success=True)

    # Render the custom question builder form
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
    questions = session.get('custom_game_questions', [])  # List of questions for the current custom set
    index = session.get('custom_current_index', 0)        # Current question index
    score = session.get('custom_score', 0)                # Current score

    # If all questions have been answered, show results
    if index >= len(questions):
        return render_template('results.html', player_score=score)

    current_question = questions[index]  # Get the current question
    feedback = None

    if request.method == 'POST':
        selected = int(request.form.get("answer", -1))  # Get the selected answer index from the form
        if selected == current_question['answer']:
            feedback = {"correct": True, "message": "Correct!"}  # Correct answer feedback
            score += 1
        else:
            feedback = {"correct": False, "message": "Wrong!"}  # Wrong answer feedback

        index += 1
        session['custom_current_index'] = index  # Update session with new index
        session['custom_score'] = score          # Update session with new score

        # If all questions have been answered after this answer, save result and show results page
        if index >= len(questions):
            set_title = session.get('current_custom_set', 'Default')
            save_game_result(score, set_title)  # Save the game result to the database

            local_scores = session.get('local_scores', [])
            local_scores.append({
                "player": session.get('player_name', 'Anonymous'),
                "score": score,
                "game": set_title
            })
            session['local_scores'] = local_scores

            return render_template('results.html', player_score=score)

        current_question = questions[index]  # Move to the next question

    # Render the question page with current question, feedback, and score
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
