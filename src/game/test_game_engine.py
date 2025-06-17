from game_engine import GameEngine
from game.Question import Question
import pytest

def test_game_engine_initialization():
    engine = GameEngine()
    assert engine.get_score() == 0
    assert engine.get_total_questions() == 0
    assert not engine.has_more_questions()

def test_game_engine_load_questions():
    engine = GameEngine()
    engine.load_questions_json()  # Assuming this method populates questions
    assert engine.get_total_questions() > 0  # Ensure questions are loaded
    assert engine.has_more_questions()

def test_game_engine_submit_answer():
    engine = GameEngine()
    engine.load_questions_json()  # Load questions first
    question = engine.get_current_question()
    
    if question:
        correct_answer_index = question.answer
        assert engine.submit_answer(correct_answer_index) is True  # Correct answer
        assert engine.get_score() == 1  # Score should increase by 1

        # Submit an incorrect answer
        wrong_answer_index = (correct_answer_index + 1) % len(question.options)
        assert engine.submit_answer(wrong_answer_index) is False  # Incorrect answer
        assert engine.get_score() == 1  # Score should remain the same
    else:
        pytest.skip("No questions available for testing.")

def test_game_engine_get_current_question():
    engine = GameEngine()
    engine.load_questions_json()  # Load questions first
    question = engine.get_current_question()

    print(type(question))
    
    assert question is not None  # Should return a question if available



def test_game_engine_has_more_questions():
    engine = GameEngine()
    engine.load_questions_json()  # Load questions first
    assert engine.has_more_questions() is True  # Should return True if questions are loaded



def test_game_engine_has_more_questions_2():
    engine = GameEngine()
    engine.load_questions_json()  # Load questions first

    # Simulate answering all questions
    while engine.has_more_questions():
        engine.submit_answer(0)  # Answering with index 0 for simplicity

    assert engine.has_more_questions() is False  # Should return False after all questions are answered

def test_game_engine_get_score():
    engine = GameEngine()
    engine.load_questions_json()  # Load questions first

    while engine.has_more_questions():
        engine.submit_answer(0)
    
    assert engine.get_score() > 0

def test_game_engine_get_total_questions():
    engine = GameEngine()
    engine.load_questions_json()  # Load questions first
    total_questions = engine.get_total_questions()
    
    assert total_questions > 0  # Should return a positive number if questions are loaded
    assert isinstance(total_questions, int)  # Should return an integer


def test_game_engine_load_questions_json():
    engine = GameEngine()
    engine.load_questions_json()  # Assuming this method populates questions
    assert engine.get_total_questions() > 0  # Ensure questions are loaded


def test_game_engine_load_questions_json_2():
    engine = GameEngine()
    engine.load_questions_json()  # Assuming this method populates questions
    assert isinstance(engine.questions, list)  # Should be a list of Question objects
    
def test_game_engine_load_questions_json_3():
    engine = GameEngine()
    engine.load_questions_json()  # Assuming this method populates questions
    print(type(engine.questions[0]))
    assert type(engine.questions[0]) == Question  # Should be a list of Question objects


def test_game_engine_load_questions_json_4():
    engine = GameEngine()
    engine.load_questions_json()  # Assuming this method populates questions
    assert len(engine.questions) > 0  # Should have loaded at least one question
    assert isinstance(engine.questions[0], Question)  # First item should be a Question object

