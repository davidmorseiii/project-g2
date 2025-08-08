# API Reference – Project-G2 Trivia Game

This document describes the main classes, functions, and routes in the Project-G2 Trivia Game codebase.

---

## Flask App (`src/app.py`)

### Routes

- `/` – Home page. Renders `index.html`.
- `/scoreboard` – Displays the scoreboard from the database.
- `/enter-name` – Handles player name input and game mode selection.
- `/start` – Main gameplay loop for the default question set.
- `/custom` – Allows players to build and save a custom question set.
- `/custom-game-play` – Plays through a custom question set.
- `/start-custom` – Begins gameplay for a selected custom set.
- `/custom-sets` – Displays available custom sets.
- `/debug-session` – Returns current session data (debug only).
- `/clear-session` – Clears all session data (debug only).

#### Helper Functions
- `save_game_result(player_score, set_title="Default")`
  - Saves a player's game result to the database. Creates a new `QuestionSet` if needed.

---

## Models (`src/models.py`)

### User
Represents a player/user of the game.
- `id`: int, primary key
- `username`: str, unique

### QuestionSet
Represents a set of trivia questions (default or custom).
- `id`: int, primary key
- `title`: str
- `creator_id`: int (User.id)

### Question
Represents a single trivia question.
- `id`: int, primary key
- `prompt`: str
- `options`: list[str]
- `answer`: int (index of correct option)
- `set_id`: int (QuestionSet.id)

### GameResult
Represents a completed game session and score.
- `id`: int, primary key
- `user_id`: int (User.id)
- `set_id`: int (QuestionSet.id)
- `score`: int

---

## Game Logic (`src/game/game_engine.py`)

### GameEngine
Handles the main game state and logic.

#### Methods:
- `load_questions_json(path: str = None)`
  - Loads questions from a JSON file. Default path if not provided.
- `get_current_question()`
  - Returns the current `Question` object.
- `has_more_questions()`
  - Returns True if there are more questions to play.

---

## Question (`src/game/question.py`)

### Question
Represents a trivia question.

#### Parameters:
- `prompt`: str – The question text.
- `options`: list[str] – List of answer choices.
- `answer`: int – Index of the correct answer (0-based).

#### Methods:
- `is_correct(choice: int) -> bool` – Returns True if the given choice is correct.
- `__str__()` – Returns a string representation of the question.

---

## Question Repository (`src/game/question_repository.py`)

### QuestionRepository
Loads and manages question sets from JSON files.

#### Methods:
- `load(path: str)` – Loads questions from a JSON file.
- `save(path: str)` – Saves questions to a JSON file.

---

## CLI Interface (`src/game/cli.py`)

### CLIInterface
Handles command-line gameplay.

#### Methods:
- `display_question()` – Shows a question and options.
- `get_user_choice()` – Gets and validates user input.
- `run()` – Main loop for CLI gameplay.

---

## Testing
- Unit tests are in `src/game/test_Question.py`, `src/game/test_game_engine.py`, and `src/game/test_cli.py`.

---

## JSON Schema for Questions

```json
{
  "category": "string",
  "prompt": "string",
  "options": ["string", "string", "string", "string"],
  "answer": 0
}
```

---

For more details, see inline docstrings in each module.
