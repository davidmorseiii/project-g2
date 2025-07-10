from flask import Flask, render_template, request, session
from game.game_engine import GameEngine

app = Flask(__name__)
app.secret_key = "dev.secret" # this is needed for session storage

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/start', methods=['GET', 'POST'])
def display_question():
    #placeholder question until we load from engine
    
      # Load questions from JSON file
    question = {
        "prompt": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"]
    }

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
        
        # correct_answer = 2 #Paris
        if selected and question.is_correct(selected):
            feedback = { "correct": True, "message": "Correct!" }
            player_score += 1
        else:
            feedback = { "correct": False, "message": "Wrong! Try again." }
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

@app.route('/custom')
def custom_game():
    """
    In memory collector for custom questions.
    Session list to be replaced with SQLite persistence later.
    """
    if request.method == 'POST':
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

        # store in memory for now
        custom_qs = session.get('custom_questions', [])
        custom_qs.append(q)
        session['custom_questions'] = custom_qs

        # re-render template with success flag
        return render_template('custom_game.html', success=True)
    
    return render_template('custom_game.html', success=False)

@app.route('/results')
def results():
    return render_template("results.html", player_score=0)

if __name__ == '__main__':
    app.run(debug=True)