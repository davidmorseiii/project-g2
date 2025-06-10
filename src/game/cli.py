from .engine import GameEngine
import os

class CLIInterface:
    def __init__(self):
        self.engine = GameEngine()

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
        