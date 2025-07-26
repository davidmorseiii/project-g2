from flask import Flask, render_template, request, session, redirect
from flask.views import MethodView
from game.game_engine import GameEngine
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'  # Moved above init_app
app.secret_key = "dev.secret"  # Needed for session storage

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

    
@app.route('/scoreboard')
def scoreboard():
    return render_template("scoreboard.html")

@app.route('/start', methods=['GET', 'POST'])
def display_question():

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
    if request.args.get('reset') == 'true':
        session.pop('custom_set_name', None)
        session.pop('custom_questions', None)
        return render_template('custom_game.html', success=False)

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
            return render_template('results.html', player_score=score)
        current_question = questions[index]

    return render_template("start.html", question=current_question, feedback=feedback,
                           player_score=score, current_question=index)

@app.route('/start-custom', methods=['POST'])
def start_custom():
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
    sets = session.get('all_custom_sets', {})
    return render_template('choose_custom_set.html', sets=sets.keys())

if __name__ == '__main__':
    app.run(debug=True)
