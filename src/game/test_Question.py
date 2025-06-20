from game.question import Question
import pytest

def test_question_initialization():
    question_data = {
        "category": "Science",
        "prompt": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
        "answer": 0
    }
    question = Question(question_data)
    
    assert question.category == "Science"
    assert question.prompt == "What is the chemical symbol for water?"
    assert question.options == ["A) H2O", "B) CO2", "C) O2", "D) NaCl"]
    assert question.answer == 0

def test_question_is_correct():
    question_data = {
        "category": "Science",
        "prompt": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
        "answer": 0
    }
    question = Question(question_data)
    
    assert question.is_correct("a") is True  # Correct answer as string
    assert question.is_correct(0) is True     # Correct answer as integer
    assert question.is_correct("b") is False  # Incorrect answer as string
    assert question.is_correct(1) is False     # Incorrect answer as integer
    assert question.is_correct("e") is False   # Invalid answer, should return False

def test_question_answer_to_index():
    question_data = {
        "category": "Science",
        "prompt": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
        "answer": 0
    }
    question = Question(question_data)
    
    assert question.answer_to_index("a") == 0
    assert question.answer_to_index("b") == 1
    assert question.answer_to_index("c") == 2
    assert question.answer_to_index("d") == 3
    assert question.answer_to_index("e") is None  # Invalid answer, should return None

def test_question_str():
    question_data = {
        "category": "Science",
        "prompt": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
        "answer": 0
    }
    question = Question(question_data)
    
    expected_str = (
        "Category: Science\n"
        "What is the chemical symbol for water?\n"
        "A) H2O\n"
        "B) CO2\n"
        "C) O2\n"
        "D) NaCl"
    )
    
    assert str(question) == expected_str

def test_question_invalid_answer_type():
    question_data = {
        "category": "Science",
        "prompt": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
        "answer": 0
    }
    question = Question(question_data)
    
    with pytest.raises(ValueError):
        question.is_correct(3.14)  # Invalid type, should raise TypeError

def test_question_invalid_answer_string():
    question_data = {
        "category": "Science",
        "prompt": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
        "answer": 0
    }
    question = Question(question_data)
    
    assert question.is_correct("e") is False  # Invalid answer, should return False