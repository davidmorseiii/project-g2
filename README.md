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

## How to Run

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-directory>

## File Structure
main.py                 - Entry point of the application (Luke)
question.py              - Defines the Question class (Curtis)
game_engine.py           - Manages game state and scoring (David)
cli_interface.py         - Handles user interaction (Luke)
question_repository.py   - Loads questions from a JSON file (Taylor)
questions.json           - Sample questions for testing (Taylor)
tests/                   - Unit tests for all modules (Curtis)
README.txt               - This file
