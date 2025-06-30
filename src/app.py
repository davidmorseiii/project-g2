from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/start', methods=['GET', 'POST'])
def display_question():
    #placeholder question until we load from engine
    question = {
        "prompt": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"]
    }

    feedback = None
    player_score = int(request.form.get("current_score", 0))

    if request.method == 'POST':
        selected = request.form.get("answer")
        correct_answer = 2 #Paris
        if selected and int(selected) == correct_answer:
            feedback = { "correct": True, "message": "Correct!" }
            player_score += 1
        else:
            feedback = { "correct": False, "message": "Wrong! Try again." }

    return render_template(
        "start.html",
        question=question,
        feedback=feedback,
        player_score=player_score 
    )

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)