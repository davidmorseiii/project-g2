# Project-G2 Trivia CLI Game

## Overview
This is a command-line based trivia game written in Python. The game loads multiple-choice questions from a JSON file and quizzes the player one question at a time. It tracks the player's score, gives feedback after each answer, and shows the final results at the end. The project is designed to be modular and will eventually support a graphical user interface (GUI) in a future release.

## Features
- Loads questions from a JSON file
- Presents multiple-choice questions one at a time
- Tracks and displays the player’s score
- Simple command-line interface (CLI)
- Modular codebase prepared for future GUI expansion

## Requirements
- Python 3.8 or higher

## File Structure
- `main.py` – Entry point of the application (**Luke**)
- `question.py` – Defines the `Question` class (**Curtis**)
- `game_engine.py` – Manages game state and scoring (**David**)
- `cli_interface.py` – Handles user interaction (**Luke**)
- `question_repository.py` – Loads questions from a JSON file (**Taylor**)
- `questions.json` – Sample questions for testing (**Taylor**)
- `tests/` – Unit tests for all modules (**Curtis**)
- `README.txt` – This file

## How to Run
Run in terminal to start program
```bash
python3 src/main.py
```


## Project management link
- [Taiga Link](https://taiga.luke-merrill.com/project/project-g2/backlog)
- [unit_test_spreadsheet](https://docs.google.com/spreadsheets/d/1E8BiflJdZtr32lMwURZAU-tqDZDZ60ykgGHYlUxTroA/edit?gid=0#gid=0)

### 1. Clone the Repository
```bash
git clone https://github.com/davidmorseiii/project-g2.git
```
## 2. Navigate to the file
```bash
cd project-g2
cd src
```
## 3. Run the Program
```bash
python3 main.py
```
Notes.. you must have python installed on your computer


