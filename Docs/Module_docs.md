# Module Documentation – Project-G2 Trivia Game

This document provides module-level docstrings and summaries for all major Python files in the project.

---

## src/app.py
"""
Main Flask application for the Project-G2 Trivia Game web app.
Handles all web routes, session management, and integration with the database and game logic.
"""

## src/models.py
"""
SQLAlchemy ORM models for users, question sets, questions, and game results.
Defines the database schema for the trivia game.
"""

## src/game/game_engine.py
"""
GameEngine class manages the state and logic of a trivia game session.
Handles question loading, answer checking, and score tracking.
"""

## src/game/question.py
"""
Question class represents a single trivia question, its options, and the correct answer.
Includes methods for answer validation and string representation.
"""

## src/game/question_repository.py
"""
QuestionRepository class loads and saves question sets from JSON files.
Provides methods for reading and writing question data for both default and custom sets.
"""

## src/game/cli.py
"""
CLIInterface class provides a command-line interface for playing the trivia game.
Handles user input, question display, and game loop for terminal-based play.
"""
