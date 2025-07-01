# Project-G2 Trivia CLI Game

## Overview
Our Trivia Game is a Python-based trivia application that started as a command-line (CLI) game and is evolving into a web-based GUI version using Flask. The game quizzes the player with multiple-choice questions pulled from a JSON file, tracks the score, and presents results. The project uses a modular structure and supports expansion to multiplayer, persistent storage, and leaderboard features.

## Features
- Loads questions dynamically from a JSON file
- CLI version for terminal gameplay
- Web-based GUI built with Flask and HTML templates
- Real-time scoring and feedback
- Final results screen
- Modular structure ready for future features:
    - Multiplayer support
    - Leaderboards
    - Timed rounds
    - Difficulty filtering

## Requirements
- Python 3.8 or higher
- Flask 2.0 or higher (for GUI version)
- Web browser (for GUI version)

## File Structure
- `app.py` – Main Flask application and route controller
- `question.py` – Defines the `Question` class
- `game_engine.py` – Game logic, state handling, and score tracking
- `test_app.py` – Prototype web app and discovery
- `cli_interface.py` – CLI input/output logic for terminal-based gameplay
- `question_repository.py` – Loads and parses trivia questions from a JSON file
- `templates/` - HTML templates for the web GUI
    - `index.html` – Home screen UI
    - `start.html` – Main game interface
    - `game_over.html` – Final score screen
- `static/style.css` - Basic styles used by the GUI
- `questions.json` – Sample JSON dataset used by the game
- `tests/` – Unit tests for all modules
- `README.txt` – This file

## Wireframe Design Link:
- https://www.figma.com/design/JLD2Cb2vKWvtKR6VViuSk9/Figma-basics?node-id=1669-162202&t=NEpK1vVYwpfzj5np-1

## Project management link
- [Taiga Link](https://taiga.luke-merrill.com/project/project-g2/backlog)
- [unit_test_spreadsheet](https://docs.google.com/spreadsheets/d/1E8BiflJdZtr32lMwURZAU-tqDZDZ60ykgGHYlUxTroA/edit?gid=0#gid=0)

### 1. Clone the Repository
```bash
git clone https://github.com/davidmorseiii/project-g2.git
```

### 2. Navigate to the project directory
```bash
cd project-g2
cd src
```

### 3. (Recommended) Create a virtual environment

#### On macOS/Linux:
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

### 5. Run the Program
For CLI version:
```bash
python main.py
```
For Web GUI version:
```bash
python app.py
```

**Note:** You must have Python installed on your computer. If you do not have a `requirements.txt` file, you can skip step 4. The GUI will be accessible at http://localhost:5000 after running app.py.
