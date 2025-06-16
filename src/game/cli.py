from .game_engine import GameEngine
import os

class CLIInterface:
    def __init__(self):
        # run something to get the questions
        #pass that to the game engine
        self.engine = GameEngine()
        self.engine.load_questions_json()


    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_game(self):
        print("Welcome to the Game!")
        
        while self.engine.has_more_questions():
            self.clear()  # Clear screen

            current_question = self.engine.get_current_question()
            question_number = self.engine.current_index + 1
            total_questions = self.engine.get_total_questions()
            score = self.engine.get_score()

            # Print header
            print("=" * 40)
            print(f"Question {question_number} of {total_questions} | Score: {score}")
            print("=" * 40 + "\n")

            # Print the question
            print(str(current_question))
            
            # Get input
            ans = input("\nEnter your answer (a/b/c/d): ").strip().lower()
            while ans not in ['a', 'b', 'c', 'd']:
                print("Invalid input. Please enter a, b, c, or d.")
                ans = input("Enter your answer (a/b/c/d): ").strip().lower()

            # Check answer
            correct = self.engine.submit_answer(ans)
            if correct:
                print("\n✅ Correct!")
            else:
                correct_index = current_question.answer
                print(f"\n❌ Wrong! Correct answer was: {current_question.options[correct_index]}")

            input("\nPress Enter to continue...")

        # Final screen
        self.clear()
        print("=" * 40)
        print("🎉 Game Over!")
        print(f"Your final score: {self.engine.get_score()} / {self.engine.get_total_questions()}")
        print("=" * 40)


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