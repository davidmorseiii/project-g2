from flask import Flask, render_template, request
from game.game_engine import GameEngine

app = Flask(__name__)

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
    
    if engine.has_more_questions():
        question = engine.get_current_question()
    else:
        return render_template("results.html", player_score=player_score)

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

    return render_template(
        "start.html",
        question=question,
        feedback=feedback,
        player_score=player_score,
        current_question=current_question,
    )

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/results')
def results():
    return render_template("results.html", player_score=0)

if __name__ == '__main__':
    app.run(debug=True)