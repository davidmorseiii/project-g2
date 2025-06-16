from .game_engine import GameEngine
import os

class CLIInterface:
    def __init__(self):
        # run something to get the questions
        #pass that to the game engine
        self.engine = GameEngine()
        self.engine.load_questions_json()
        print(self.engine.questions)

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
    
    def run(self):
        self.clear()
        self.start_game()
        
        while True:
            self.display_menu()
            choice = self.get_user_input()
            
            if choice == '1':
                # Start the game logic here
                print("Starting the game...")
                # Placeholder for game logic
                break
            elif choice == '2':
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        
        # Placeholder for results display
        results = ["Result 1", "Result 2", "Result 3"]
        self.show_results(results)