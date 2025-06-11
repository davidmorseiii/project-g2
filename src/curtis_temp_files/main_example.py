import json
import random
import pygame
import os
import time


global dict_list
#-----------------------------------------------------

class Question:
    def __init__(self):
        self.category = str
        self.prompt = str
        self.options = []
        self.answer = int

    def answer_to_index(ans):
        if(ans == 'a'): return 0
        if(ans == 'b'): return 1
        if(ans == 'c'): return 2
        if(ans == 'd'): return 3

    def is_correct(self, ans):
        global dict_list
        return self.answer == self.answer_to_index(ans)
    
#-----------------------------------------------------

class QuestionRepository(Question):
    def __init__(self):
        # inherited:
        # self.category = str
        # self.prompt = str
        # self.options = []
        # self.answer = int
        self.filepath = "src\curtis_temp_files\data.json"        

    def load_from_json(self):
        with open(self.filepath) as openfile:
            self.json_object = json.load(openfile)
        global dict_list 
        dict_list = self.json_object

#-----------------------------------------------------

class GameEngine(Question):
    def __init__(self):
        # inherited:
        # self.category = str
        # self.prompt = str
        # self.options = []
        # self.answer = int
        repo = QuestionRepository()
        repo.load_from_json()
        self.score = 0
        self.current_index = 0
        self.current_ans = ""
        
        
    def ask_question(self):
        global dict_list
        self.category = dict_list[self.current_index]["category"]
        self.prompt = dict_list[self.current_index]["prompt"]
        self.options = dict_list[self.current_index]["options"]
        self.answer = dict_list[self.current_index]["answer"]
        self.questions = []
        
        print("made it to ask_question")
        print(self.category)
        print(self.prompt)
        print("a) ", self.options[0],
              "\nb) ", self.options[1],
              "\nc) ", self.options[2],
              "\nd) ", self.options[3],
              )

        print()
        
    def check_answer(self):
        self.current_ans = input ("Enter 'a', 'b', 'c', 'd', or 'q' to quit :")
        self.current_index +=1
        if (self.current_ans == self.answer):
            self.scorre+=1
    
    def is_finished(self):
        global dict_list
        if (self.current_index >= len(dict_list) -1):
            x = input("Game Over.")
            exit()

    def get_score(self):
        print("You scored: ", self.score)

#-----------------------------------------------------

class CLIInterface(GameEngine):
    def __init__(self):
        self.engine = GameEngine()
        super().__init__()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def start_game(self):
        print("Welcome to the Game!")

    def display_menu(self):
        print("1. Start Game")
        print("2. Exit")
        
    def get_user_input(self):
        choice = input("Enter your choice: ")
        return choice
    
    def show_results(self, results):
        print("Game Results:")
        for result in results:
            print(result)
    
#-----------------------------------------------------

def main():
    #from other file: from game.cli import CLIInterface
    cli = CLIInterface()
    cli.clear()
    cli.start_game()
    cli.display_menu()
    choice = cli.get_user_input()
    if int(choice) != 1:
        exit()
    print("This is the Beginning!")       

    while(not cli.is_finished()):
        cli.ask_question()    
        cli.check_answer()
        cli.clear()
        cli.get_score()
        exit()

if __name__ == "__main__":
    main()