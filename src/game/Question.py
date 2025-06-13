
import json

class Question():
    def __init__(self, my_question:str):
        self.category = my_question["category"]
        self.prompt = my_question["prompt"]
        self.options = my_question["options"]
        self.answer = my_question["answer"]

    def answer_to_index(self,ans:str):
        ans = ans.tolower()
        if ans == "a":
            return 0
        if ans == "b":
            return 1
        if ans == "c":
            return 2
        if ans == "d":
            return 3

    def is_correct(self, ans:str):
        return self.answer_to_index(ans) == self.answer

f = open('QuestionRepository.json')

data = json.load(f)

for i in data:
    thisQuestion = Question(i)

f.close()