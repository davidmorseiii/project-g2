# Group 2 Trivia Game Web App
<img width="512" height="372" alt="Trivia Game" src="https://github.com/user-attachments/assets/e4376077-8f6a-40c6-bb33-6f29b32241d6" />

Our Trivia Game is a Python-based trivia application that started as a command-line (CLI) game and is evolving into a web-based GUI version using Flask. The game quizzes the player with multiple-choice questions pulled from a JSON file, tracks the score, and presents results. The project uses a modular structure and supports expansion to multiplayer, persistent storage, and leaderboard features.

---

## Features

- CLI version for terminal gameplay
- Web-based GUI built with Flask and HTML templates
- Start a trivia game with a bank of built-in questions
- Create custom question sets directly from the UI
- Play previously created custom question sets
- Score is tracked live during gameplay
- View a scoreboard (planned extension with persistent database)
- Toggle between light and dark modes

---

## Project Structure

```
project-g2-main/
├── src/
│   ├── app.py               # Flask app and route controller
│   ├── config.py            # Configuration for database paths and Flask
│   ├── models.py            # SQLAlchemy models for users, scores, etc.
│   ├── templates/           # HTML templates (Jinja2)
│   │   ├── index.html
│   │   ├── start.html
│   │   ├── results.html
│   │   ├── custom_game.html
│   │   ├── choose_custom_set.html
│   ├── static/
│   │   └── style.css        # Shared CSS styling
│   └── game/
│       ├── game_engine.py   # Core game logic
│       ├── question.py      # Question class definition
│       └── QuestionRepository.json  # Sample questions
├── instance/
│   └── game.db              # SQLite database (used for scores and users)
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## Wireframe Design Link:

- https://www.figma.com/design/JLD2Cb2vKWvtKR6VViuSk9/Figma-basics?node-id=1669-162202&t=NEpK1vVYwpfzj5np-1
<img width="512" height="164" alt="wireframe" src="https://github.com/user-attachments/assets/65118b74-14ef-4e28-808a-b75358da5d86" />

---

## Project management link

- [Taiga Link](https://taiga.luke-merrill.com/project/project-g2/backlog)


- [unit_test_spreadsheet](https://docs.google.com/spreadsheets/d/1E8BiflJdZtr32lMwURZAU-tqDZDZ60ykgGHYlUxTroA/edit?gid=0#gid=0)

---

## Requirements

- Python 3.8 or higher
- Web browser (for GUI version)

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/davidmorseiii/project-g2.git
```

### 2. Navigate to the project directory
```bash
cd project-g2
cd src
```

### 3. Create a virtual environment (Recommended)

#### On MacOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### On Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the program

#### CLI version:
```bash
python main.py
```
#### Web GUI version:
```bash
python app.py
```

**Note:** You must have Python installed on your computer. The GUI will be accessible at http://127.0.0.1:5001 in your browser.

---

## How to Play

### Default Game
1. Click "Start" on the home page
2. Answer multiple-choice questions
3. See your final score at the end

### Custom Game
1. Click "Create Custom Game"
2. Name your question set
3. Add questions with prompts, options, and correct answer
4. Go back to the home page and click "Play Custom Game"
5. Select your set and play

---

## Future Improvements

- Persistent user accounts and authentication
- Saving custom sets and scores to the database
- Enhanced leaderboard
- Question categories and difficulty levels

## Technologies Used

- Python 3
- Flask
- HTML5, CSS3
- SQLite (via SQLAlchemy)
