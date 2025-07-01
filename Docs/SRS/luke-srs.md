# Software Requirements Specification
## For Project-G2 Trivia Game (Web GUI Version)

Version 0.1  
Prepared by Luke Merrill  
Team G2  
Date Created: June 30, 2025  

Table of Contents
=================
* [Revision History](#revision-history)
* 1 [Introduction](#1-introduction)
  * 1.1 [Document Purpose](#11-document-purpose)
  * 1.2 [Product Scope](#12-product-scope)
  * 1.3 [Definitions, Acronyms and Abbreviations](#13-definitions-acronyms-and-abbreviations)
  * 1.4 [References](#14-references)
  * 1.5 [Document Overview](#15-document-overview)
* 2 [Product Overview](#2-product-overview)
  * 2.1 [Product Perspective](#21-product-perspective)
  * 2.2 [Product Functions](#22-product-functions)
  * 2.3 [Product Constraints](#23-product-constraints)
  * 2.4 [User Characteristics](#24-user-characteristics)
  * 2.5 [Assumptions and Dependencies](#25-assumptions-and-dependencies)
  * 2.6 [Apportioning of Requirements](#26-apportioning-of-requirements)
* 3 [Requirements](#3-requirements)
  * 3.1 [External Interfaces](#31-external-interfaces)
    * 3.1.1 [User Interfaces](#311-user-interfaces)
    * 3.1.2 [Hardware Interfaces](#312-hardware-interfaces)
    * 3.1.3 [Software Interfaces](#313-software-interfaces)
  * 3.2 [Functional](#32-functional)
  * 3.3 [Quality of Service](#33-quality-of-service)
    * 3.3.1 [Performance](#331-performance)
    * 3.3.2 [Security](#332-security)
    * 3.3.3 [Reliability](#333-reliability)
    * 3.3.4 [Availability](#334-availability)
  * 3.4 [Compliance](#34-compliance)
  * 3.5 [Design and Implementation](#35-design-and-implementation)
    * 3.5.1 [Installation](#351-installation)
    * 3.5.2 [Distribution](#352-distribution)
    * 3.5.3 [Maintainability](#353-maintainability)
    * 3.5.4 [Reusability](#354-reusability)
    * 3.5.5 [Portability](#355-portability)
    * 3.5.6 [Cost](#356-cost)
    * 3.5.7 [Deadline](#357-deadline)
    * 3.5.8 [Proof of Concept](#358-proof-of-concept)
* 4 [Verification](#4-verification)
* 5 [Appendixes](#5-appendixes)

## Revision History
| Name        | Date          | Reason For Changes | Version |
|-------------|---------------|-------------------|---------|
| Luke Merrill| June 30, 2025 | Initial creation  | 0.1     |

---

## 1. Introduction

### 1.1 Document Purpose
This Software Requirements Specification (SRS) describes the requirements for the Project-G2 Trivia Game, a web-based trivia game application. The intended audience includes developers, testers, and stakeholders such as Professor Ratul.

### 1.2 Product Scope
Project-G2 Trivia Game is a web application that allows users to play a multiple-choice trivia game. The game loads questions from a JSON file, presents them one at a time, tracks the player's score, and provides feedback. The application is designed to be modular and will support future enhancements such as multiplayer mode and persistent leaderboards.

### 1.3 Definitions, Acronyms and Abbreviations
- **GUI**: Graphical User Interface  
- **CLI**: Command-Line Interface  
- **JSON**: JavaScript Object Notation  
- **Flask**: A micro web framework for Python

### 1.4 References
- [Flask documentation](https://flask.palletsprojects.com/en/stable/)
- [Jinja2 documentation](https://jinja.palletsprojects.com/en/stable/)
- [Project GitHub repository](https://github.com/davidmorseiii/project-g2.git)

### 1.5 Document Overview
Section 2 provides a high-level overview of the product and its environment. Section 3 details all functional and non-functional requirements. Section 4 describes verification strategies. Section 5 contains appendices and supporting materials.

---

## 2. Product Overview

### 2.1 Product Perspective
This project is an evolution of a previously developed CLI trivia game. The current version uses Flask to provide a web-based GUI, reusing core game logic from the CLI version.

### 2.2 Product Functions
- Load trivia questions from a JSON file.
- Display questions and multiple-choice answers.
- Accept user input via web forms.
- Provide immediate feedback on answers.
- Track and display player scores.
- Show a final score summary at the end of the game.

### 2.3 Product Constraints
- Must use Python 3.8+ and Flask.
- No persistent database; questions are loaded from a static JSON file.
- Initially designed for single-player mode.
- Must be hosted on a server provided by Luke Merrill.

### 2.4 User Characteristics
Target users include students, instructors, and the general public. No technical expertise is required to use the game.

### 2.5 Assumptions and Dependencies
- The game will be accessed via a modern web browser.
- Flask and Python 3.8+ are installed on the host server.
- Hosting and domain are managed by Luke Merrill.

### 2.6 Apportioning of Requirements
All core gameplay and GUI features are included in this version. Features such as multiplayer, authentication, and persistent leaderboards may be added in future releases.

---

## 3. Requirements

### 3.1 External Interfaces

#### 3.1.1 User Interfaces
- `index.html`: Welcome screen with Start, Scoreboard, and Quit buttons.
- `start.html`: Displays questions, answer options, feedback, and score.
- `game_over.html`: Shows final score and replay option.

#### 3.1.2 Hardware Interfaces
None required.

#### 3.1.3 Software Interfaces
- Flask 2.0+  
- Python 3.8+  
- Browser interface (HTML/CSS/JS rendered with Jinja2)  
- Static JSON file: `questions.json`

### 3.2 Functional
F1. Load trivia questions from JSON at game start.  
F2. Display one question at a time with four answer choices.  
F3. Allow user to select and submit an answer.  
F4. Check answer and update score.  
F5. Provide immediate feedback (Correct/Wrong).  
F6. Proceed to next question after feedback.  
F7. End game when all questions are answered.  
F8. Display final score summary.  
F9. Render score tracking UI.  
F10. Render all templates through Flask with proper variable context.  
F11. (Future) Support multiplayer mode.

### 3.3 Quality of Service

#### 3.3.1 Performance
Each page should load within 1 second on a standard local network.

#### 3.3.2 Security
No personal data is stored. Input should be sanitized if multiplayer or persistence is added.

#### 3.3.3 Reliability
The game should not crash during normal use.

#### 3.3.4 Availability
The web app should be available whenever the host server is running.

### 3.4 Compliance
No formal compliance requirements.

### 3.5 Design and Implementation

#### 3.5.1 Installation
To install and run the application on any platform:
```bash
# Create a virtual environment (cross-platform)
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

#### 3.5.2 Distribution
Distributed via GitHub and hosted on Luke's server.

#### 3.5.3 Maintainability
Code is modular (GameEngine, Question, Templates). Templates use Jinja2 for clarity.

#### 3.5.4 Reusability
Game logic is reusable for both CLI and GUI versions.

#### 3.5.5 Portability
Runs on any OS with Python and Flask.

#### 3.5.6 Cost
No monetary cost. Server space and domain provided by Luke Merrill.

#### 3.5.7 Deadline
Due: August 8th, 2025.

#### 3.5.8 Proof of Concept
A working CLI version exists. Flask version will reuse core logic.

---

## 4. Verification
- Manual gameplay testing.
- Unit tests for GameEngine and Question logic.
- Browser-based testing of templates.
- Route tests to confirm correct Flask behavior.

---

## 5. Appendixes
- Sample JSON file: `questions.json`
- Screenshot of wireframe design (see design document)
- Meeting reports (see meeting_reports/ folder)

---

**Prepared by Luke Merrill, Team G2**