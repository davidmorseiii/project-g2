
import json

class Question():
    def __init__(self, my_question:str):
        self.category = my_question["category"]
        self.prompt = my_question["prompt"]
        self.options = my_question["options"]
        self.answer = my_question["answer"]

    def answer_to_index(self,ans:str):
        ans = ans.lower()
        if ans == "a": return 0
        if ans == "b": return 1
        if ans == "c": return 2
        if ans == "d": return 3

    def is_correct(self, ans:str):
        return self.answer_to_index(ans) == self.answer
    
    def __str__(self):
        opts = "\n".join(self.options)
        return f"Category: {self.category}\n{self.prompt}\n{opts}"


#Question testing

# q = Question({
#     "category": "Science",
#     "prompt": "What is the chemical symbol for water?",
#     "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
#     "answer": 0
# })

# print(q)
# print(q.is_correct("a"))  # Should return True
# print(q.is_correct("b"))  # Should return False
# print(q.answer_to_index("a"))  # Should return 0    