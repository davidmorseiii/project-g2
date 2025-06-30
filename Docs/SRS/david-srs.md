# Software Requirements Specification
## For Trivia Game (Web GUI Version)

Version 0.1  
Prepared by David Morse  
Team G2  
Date Created: 2025-06-29

---

## Revision History
|     Name    |     Date     |     Reason For Changes     | Version |
|-------------|--------------|----------------------------|---------|
| David Morse |  2025-06-29  |     Initial SRS Draft      |   0.1   |

---

## 1. Introduction

### 1.1 Document Purpose
This Software Requirements Specification (SRS) defines the functional and non-functional requirements for a Python-based web trivia game application. It is intended for developers, testers, and Professor Ratul.

### 1.2 Product Scope
The Trivia Game is a web-based application that allows user to play a multiple-choice trivia game. The game loads questions from a JSON file, tracks the player's score, and provides feedback. The original prototype was CLI-based, but this version includes a GUI with Flask and hosted on a web server. The game will eventually support two players.

### 1.3 Definitions, Acronyms and Abbreviations
- GUI: Graphical User Interface  
- CLI: Command-Line Interface  
- JSON: JavaScript Object Notation  
- Flask: A micro web framework for Python

### 1.4 References
- Flask documentation: https://flask.palletsprojects.com/en/stable/
- Jinja2 documentation: https://jinja.palletsprojects.com/en/stable/
- Project GitHub repository: https://github.com/davidmorseiii/project-g2.git

### 1.5 Document Overview
Section 2 describes the product and its environment. Section 3 details all software requirements. Section 4 discusses verification strategies. Section 5 contains appendices.

---

## 2. Product Overview

### 2.1 Product Perspective
This is a new version of a previously approved CLI trivia game prototype. It replaces the CLI with a web GUI using Flask and HTML templates. Game logic is reused from the previous milestone.

### 2.2 Product Functions
- Load and parse a JSON file of trivia questions.
- Display each question with four possible answers.
- Accept user input via radio buttons.
- Check answers and display immediate feedback.
- Track and display player scores.
- Present a final score summary screen.

### 2.3 Product Constraints
- Must use Python and Flask.
- Must be hosted using a custom domain (provided by Luke).
- No persistent database storage (questions loaded from JSON).
- Designed initially for single-player mode.

### 2.4 User Characteristics
Target users are classmates, instructors, and friends. No technical background required to use the interface.

### 2.5 Assumptions and Dependencies
- The game will run in a modern browser.
- Flask and Python 3.8+ are installed on the server.
- Hosting is handled by a Luke Merrill

### 2.6 Apportioning of Requirements
Currently includes all GUI and gameplay features. Future versions may include a multiplayer mode, authentication, or leaderboard persistence.

---

## 3. Requirements

### 3.1 External Interfaces

#### 3.1.1 User Interfaces
- `index.html`: welcome screen with Start, Scoreboard, and Quit buttons.
- `start.html`: question display with radio buttons for answers, feedback, and score.
- `game_over.html`: final score display and replay button.

#### 3.1.2 Hardware Interfaces
None.

#### 3.1.3 Software Interfaces
- Flask 2.0+
- Python 3.8+
- Browser interface (HTML/CSS/JS rendered with Jinja2)
- Static JSON question file: `QuestionRepository.json`

### 3.2 Functional
F1. Load trivia questions from JSON on game start.  
F2. Display one question at a time with 4 answer choices.  
F3. Allow user to select and submit an answer.  
F4. Check answer and update score.  
F5. Provide visual feedback: Correct / Wrong.  
F6. Proceed to next question after feedback.  
F7. End game when no questions remain.  
F8. Display final score summary.  
F9. Render score tracking UI (ex: “Player1 Score: X”).  
F10. Render all templates through Flask with proper variable context.  
F11. (Future) Track multiple players.

### 3.3 Quality of Service

#### 3.3.1 Performance
The app should render each page within 1 second over a standard local network.

#### 3.3.2 Security
No personal data is stored. Server should sanitize user input if multiplayer or persistence is added later.

#### 3.3.3 Reliability
The game should never crash during normal question flow.

#### 3.3.4 Availability
The web app should be available as long as the host server is running.

### 3.4 Compliance
No formal compliance required.

### 3.5 Design and Implementation

#### 3.5.1 Installation
Run `pip install -r requirements.txt` and `python app.py`

#### 3.5.2 Distribution
Distributed via GitHub and hosted on Luke's server.

#### 3.5.3 Maintainability
Code is modular (GameEngine, Question, Templates). Templates will use Jinja2 for clarity.

#### 3.5.4 Reusability
Game logic is reusable for both CLI and GUI versions.

#### 3.5.5 Portability
Runs on any OS with Python and Flask.

#### 3.5.6 Cost
No monetary cost. Server space and domain provided free by Luke Merrill.

#### 3.5.7 Deadline
Due: August 8th, 2025.

#### 3.5.8 Proof of Concept
A working CLI version exists. Flask version will reuse core logic.

---

## 4. Verification
- Manual testing of gameplay.
- Unit tests for GameEngine and Question logic.
- Browser-based testing of templates.
- Route tests to confirm correct Flask behavior.

---

## 5. Appendixes
- Sample JSON file: `QuestionRepository.json`
- Screenshot of wireframe design (see design document)
- Meeting reports (see meeting_reports/ folder)

