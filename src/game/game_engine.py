import json
import os
from game.question import Question

class GameEngine:
    def __init__(self):
        """
        Initialize game engine with a list of Question objects.
        Sets up an empty question list, current index, and score.
        """
        self.questions = []
        self.current_index = 0
        self.score = 0

    def has_more_questions(self):
        """
        Returns True if there are still questions left in the game.
        """
        return self.current_index < len(self.questions)

    def get_current_question(self):
        """
        Returns current Question object, or None if no more questions.
        """
        if self.has_more_questions():
            # print(self.questions[self.current_index])
            # print(f"Current index: {self.current_index}, Total questions: {len(self.questions)}")
            return self.questions[self.current_index]
        return None

    def submit_answer(self, answer_index):
        """
        Submits an answer for the current question.
        Returns True if correct, False otherwise.
        Moves to the next question after submitting.
        """
        current_question = self.get_current_question()
        if current_question is None:
            return False  # no question to answer

        is_correct = current_question.is_correct(answer_index)
        if is_correct:
            self.score += 1

        self.current_index += 1  # move to next question
        return is_correct

    def get_score(self):
        """
        Returns current score as an integer.
        """
        return self.score

    def get_total_questions(self):
        """
        Returns total number of questions in the game.
        """
        return len(self.questions)
    
    def load_questions_json(self):
        """
        Loads questions from a JSON file.
        Tries several possible paths for the question repository file.
        Populates self.questions with Question objects.
        Raises FileNotFoundError if no file is found.
        """
        paths_to_try = [
            "QuestionRepository.json", 
            "game/QuestionRepository.json", 
            "src/game/QuestionRepository.json"
        ]

        for path in paths_to_try:
            if os.path.exists(path):
                with open(path, "r") as f:
                    data = json.load(f)
                    self.questions = [Question(q) for q in data]  # Create Question objects from JSON
                return

        # If no file found, raise error
        raise FileNotFoundError("QuestionRepository.json not found in either location.")


