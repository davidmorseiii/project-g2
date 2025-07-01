# Software Requirements Specification

## For G2 Trivia Game (Web GUI Version)

Version 1.0
Prepared by Group G2
Date: June 30, 2025

---

## Revision History

|   Name   |    Date    |              Reason For Changes              | Version |
|----------|------------|----------------------------------------------|---------|
| Group G2 | 2025-06-30 | Merged and refined SRS from all team members |   1.0   |

---

## 1. Introduction

### 1.1 Document Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the G2 Trivia Game project. This web-based application provides a GUI for a multiple-choice trivia game. It replaces a previous CLI version and is intended for developers, testers, and professor Ratul.

### 1.2 Product Scope

The G2 Trivia Game is a Flask-based web app where users answer multiple-choice trivia questions loaded from a JSON file. It tracks player scores, provides immediate feedback, and ends with a final score summary. Future versions may support multiplayer, persistent storage, and leaderboards.

### 1.3 Definitions, Acronyms and Abbreviations

- **GUI**: Graphical User Interface
- **CLI**: Command-Line Interface
- **JSON**: JavaScript Object Notation
- **Flask**: A micro web framework for Python

### 1.4 References

- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/en/stable/)
- Project GitHub Repo: (https://github.com/davidmorseiii/project-g2.git)

### 1.5 Document Overview

Section 2 introduces the product and users. Section 3 contains requirements. Section 4 outlines verification. Section 5 contains appendices.

---

## 2. Product Overview

### 2.1 Product Perspective

This is a web-based version of a CLI trivia prototype. It uses HTML templates, Flask routing, and JSON data loading. The game logic remains modular.

### 2.2 Product Functions

- Load and parse questions from JSON
- Display question and four answer choices
- Accept and validate user input
- Provide immediate feedback
- Track and display scores
- Show final score screen

### 2.3 Product Constraints

- Python 3.8+ and Flask are required
- Static question file (no database)
- Will be hosted using a server provided by Luke
- Initially single-player

### 2.4 User Characteristics

Users include students, professors, and general players. No technical knowledge is required.

### 2.5 Assumptions and Dependencies

- Access via modern browser
- Host has Python 3.8+ and Flask installed
- JSON file is preformatted and valid

### 2.6 Apportioning of Requirements

Core gameplay and GUI are in this version. Multiplayer, persistent scores, and accounts are deferred.

---

## 3. Requirements

### 3.1 External Interfaces

#### 3.1.1 User Interfaces

- `index.html`: Home screen with Start, Scoreboard, and Quit options
- `start.html`: Displays question, answers, and score

#### 3.1.2 Hardware Interfaces

None required.

#### 3.1.3 Software Interfaces

- Flask 2.0+
- Python 3.8+
- HTML/CSS (with Jinja2)
- `QuestionRepository.json`

### 3.2 Functional Requirements

F1. Load trivia questions from JSON on start\
F2. Display a single question with 4 answer choices\
F3. Accept and validate answer submission\
F4. Update score based on correctness\
F5. Provide visual feedback (correct/wrong)\
F6. Move to next question on submit\
F7. End game after final question\
F8. Show final score and results\
F9. Render UI dynamically with Flask\
F10. Scoreboard tracks player points\
F11. (Future) Multiplayer support\
F12. (Future) Timed questions\
F13. (Future) Leaderboard persistence\
F14. (Future) Replay functionality\
F15. (Future) Difficulty filtering

### 3.3 Quality of Service Requirements

#### 3.3.1 Performance

Pages should load in < 1s over standard Wi-Fi.

#### 3.3.2 Security

No sensitive data stored. Sanitize input in future multiplayer version.

#### 3.3.3 Reliability

App should run error-free through entire question set.

#### 3.3.4 Availability

App is available as long as server is online.

### 3.4 Compliance

No special compliance requirements.

### 3.5 Design and Implementation

#### 3.5.1 Installation

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

#### 3.5.2 Distribution

Self hosted with Flask. Will be hosted via server provided by Luke Merrill in the future. Code on GitHub.

#### 3.5.3 Maintainability

Codebase modular (GameEngine, Questions, CLI, Templates)

#### 3.5.4 Reusability

Game logic shared between CLI and Flask GUI

#### 3.5.5 Portability

Cross-platform with Python

#### 3.5.6 Cost

No monetary costs

#### 3.5.7 Deadline

Due: August 8th, 2025

#### 3.5.8 Proof of Concept

CLI version complete. Web version uses same logic base.

---

## 4. Verification

- Unit tests for game engine and logic
- Manual testing of all routes and template rendering
- Browser-based interaction test

---

## 5. Appendices

- `QuestionRepository.json` example format
- Wireframe mockups (see GUI design doc)
- Meeting notes and sprint reports

---

**Prepared by Team G2: David Morse, Luke Merrill, Taylor Hodson**

