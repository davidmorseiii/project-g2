from cli import CLIInterface
import pytest


def test_cli_load():
    cli = CLIInterface()
    
    # Test initial state
    assert cli.engine.get_score() == 0
    assert cli.engine.get_total_questions() > 0  # Assuming questions are loaded


def test_cli_load_questions():
    cli = CLIInterface()
    cli.engine.load_questions_json()  # Assuming this method populates questions
    assert cli.engine.get_total_questions() > 0  # Ensure questions are loaded


