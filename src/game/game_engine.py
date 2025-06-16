import json
from .Question import Question

class GameEngine:
    def __init__(self):
        """
        Initialize game engine with a list of Question objects.
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
            return False  # No question to answer

        is_correct = current_question.is_correct(answer_index)
        if is_correct:
            self.score += 1

        self.current_index += 1  # Move to next question
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
        with open("src/QuestionRepository.json", "r") as f:
            import json
            data = json.load(f)
            self.questions = [Question(q) for q in data]
        # print(f"Loaded {len(self.questions)} questions.")
        # for q in self.questions:
        #     print(q)
  
