import json
import random
import pygame
import os
import time

# Do not change after assigned in QuestionRepository
# Created this variable to follow UML doc.
global DICT_LIST_CONST         
#-----------------------------------------------------

# Create Question Object
class Question:
    def __init__(self):
        self.category = str
        self.prompt = str
        self.options = []
        self.answer = int
        
    # Changes string to int index
    def answer_to_index(self, ans):
        if(ans == 'a'): return 0
        if(ans == 'b'): return 1
        if(ans == 'c'): return 2
        if(ans == 'd'): return 3
    
    # Returns True/False if ans == answer index in DICT_LIST_CONST
    def is_correct(self, ans):
        global DICT_LIST_CONST
        return self.answer == self.answer_to_index(ans)
    
#-----------------------------------------------------

# Create shareable list of dictionaries 
# (when imported the dictionaries are same exact format as
# Question object would be.  We could encapsulate these by
# creating a list of question objects that are only accessable
# by methods but this follows the UML doc.)
class QuestionRepository(Question):
    def __init__(self):
        # inherited:
        # self.category = str
        # self.prompt = str
        # self.options = []
        # self.answer = int

        # answer_to_index(ans)
        # is_correct(self, ans)

        self.filepath = "src\curtis_temp_files\data.json"        

    # Method to create a list of dictionaries (a question repository)
    def load_from_json(self):
        with open(self.filepath) as openfile:
            self.json_object = json.load(openfile)
        global DICT_LIST_CONST 
        DICT_LIST_CONST = self.json_object

#-----------------------------------------------------

class GameEngine(Question):
    def __init__(self):
        # Inherited:
        # self.category = str
        # self.prompt = str
        # self.options = []
        # self.answer = int

        # answer_to_index(ans)
        # is_correct(self, ans)

        self.score = 0
        self.current_index = 0
        self.current_ans = ""
        repo = QuestionRepository()
        repo.load_from_json()
        
    # initialize all variables for 1 question, print question to screen
    def ask_question(self):
        global DICT_LIST_CONST
        self.category = DICT_LIST_CONST[self.current_index]["category"]
        self.prompt = DICT_LIST_CONST[self.current_index]["prompt"]
        self.options = DICT_LIST_CONST[self.current_index]["options"]
        self.answer = DICT_LIST_CONST[self.current_index]["answer"]
        self.questions = []
        print("Score :  ", self.score)
        print(self.category)
        print(self.prompt)
        print("a) ", self.options[0],
              "\nb) ", self.options[1],
              "\nc) ", self.options[2],
              "\nd) ", self.options[3],
              )

        print()
    
    # Get and check answer, increase score if correct
    def check_answer(self):
        self.current_ans = input ("Enter 'a', 'b', 'c', 'd', or 'q' to quit :")
        self.current_index +=1
    # Must account for 2 values not being compareable such as str and int, used if()
        if (self.answer_to_index(self.current_ans) != self.answer):
            pass
        else:
            self.score+=1
    
    # If all questions are answered, end game, return True to end game loop
    def is_finished(self):
        global DICT_LIST_CONST
        if (self.current_index >= len(DICT_LIST_CONST) -1):
            print("Congratulations you have answered all questions!")
            print("             -- Game Over--")
            input("          (press any key to continue)")
            return True
        elif self.current_ans == 'q': 
            return True
        return False

    # Return score
    def get_score(self):
        return self.score

#-----------------------------------------------------

class CLIInterface(GameEngine):
    def __init__(self):
        self.engine = GameEngine()
        self.results = self.engine.get_score()             #no results found yet
        # Inherited:
        # Inherited:
        # self.category = str
        # self.prompt = str
        # self.options = []
        # self.answer = int
        # answer_to_index(ans)
        # is_correct(self, ans)
        # self.score = 0
        # self.current_index = 0
        # self.current_ans = ""
        # ask_question(self)
        # check_answer(self)
        # is_finished(self)
        # get_score(self)

    # This needs comments
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Start game, print welcome
    def start_game(self):
        print("Welcome to the Game!")

    # Display choices
    def display_menu(self):
        print("1. Start Game")
        print("2. Exit")
        
    # Get input, return
    def get_user_input(self):
        choice = input("Enter your choice: ")
        return choice
    
    # Need to create Highest Scores, save to file, pull from file
    # Show results of game
    def show_results(self):
        print("Game Results:")         
        # for result in self.results:       #<---------temporary fix
        #     print(result)
        #pass
#-----------------------------------------------------

def main():
    #create CLIInterface - which initializes engine as a GameEngine
    cli = CLIInterface()

    # use CLIInterface functions
    cli.clear()
    cli.start_game()
    cli.display_menu()
    choice = cli.get_user_input()
    if int(choice) != 1:
        exit()
    print("You have # Questions, Good Luck!")       

    # To use GameEngine functions in cli use cli.engine
    while(not cli.engine.is_finished()):
        cli.engine.ask_question()    
        cli.engine.check_answer()

    # use CLIInterface functions
        cli.clear()
    #---------------------------- <--what is show results? High Scoreboard?
    #----------------------------    we can develop this to save/pull from file
    cli.show_results()
    input("(--press enter to exit--)")

if __name__ == "__main__":
    main()