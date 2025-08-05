import time
import json

class Question():
    """
    Initialize question class.
    """
    def __init__(self, my_question:dict):
        self.category = my_question["category"]
        self.prompt = my_question["prompt"]
        self.options = my_question["options"]
        self.answer = my_question["answer"]

    def answer_to_index(self,ans:str):
        """
        Returns correct answer index.
        """
        ans = ans.lower()
        if ans == "a": return 0
        if ans == "b": return 1
        if ans == "c": return 2
        if ans == "d": return 3

    def is_correct(self, ans):
        """
        Checks if correct answer == self.answer. Raises value error if non string/integer provided.
        """
        if type(ans) is str:
            return self.answer_to_index(ans) == self.answer
        elif type(ans) is int:
            return ans == self.answer
        else:
            raise ValueError("Invalid answer type. Please provide a string or integer.")

    
    def __str__(self):
        opts = "\n".join(self.options)
        return f"Category: {self.category}\n{self.prompt}\n{opts}"