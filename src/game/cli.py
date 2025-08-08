from game.game_engine import GameEngine
import os

class CLIInterface:
    """
    Command-line interface for the Trivia Game.
    Handles user interaction, question display, and game loop for terminal-based play.
    """
    def __init__(self):
        """
        Initializes the CLI interface and loads questions into the game engine.
        """
        # Create a GameEngine instance and load questions from JSON
        self.engine = GameEngine()
        self.engine.load_questions_json()

    def clear(self):
        """
        Clears the terminal screen for better readability.
        Works on both Windows and Unix systems.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_game(self):
        """
        Main game loop for the CLI trivia game.
        Displays questions, collects user input, checks answers, and shows feedback.
        """
        print("Welcome to the Game!")
        
        while self.engine.has_more_questions():
            self.clear()  # Clear screen before each question

            current_question = self.engine.get_current_question()
            question_number = self.engine.current_index + 1
            total_questions = self.engine.get_total_questions()
            score = self.engine.get_score()

            # Print header with question number and score
            print("=" * 40)
            print(f"Question {question_number} of {total_questions} | Score: {score}")
            print("=" * 40 + "\n")

            # Print the question text and options
            print(str(current_question))
            
            # Get user input and validate
            ans = input("\nEnter your answer (a/b/c/d): ").strip().lower()
            while ans not in ['a', 'b', 'c', 'd']:
                print("Invalid input. Please enter a, b, c, or d.")
                ans = input("Enter your answer (a/b/c/d): ").strip().lower()

            # Check answer and provide feedback
            correct = self.engine.submit_answer(ans)
            if correct:
                print("\n✅ Correct!")
            else:
                correct_index = current_question.answer
                print(f"\n❌ Wrong! Correct answer was: {current_question.options[correct_index]}")

            input("\nPress Enter to continue...")

        # Final screen after all questions are answered
        self.clear()
        print("=" * 40)
        print("🎉 Game Over!")
        print(f"Your final score: {self.engine.get_score()} / {self.engine.get_total_questions()}")
        print("=" * 40)

    def display_menu(self):
        """
        Displays the main menu options to the user.
        """
        print("1. Start Game")
        print("2. Exit")
        
    def get_user_input(self):
        """
        Prompts the user for a menu choice and returns it as a string.
        """
        choice = input("Enter your choice: ")
        return choice
    
    def show_results(self, results):
        """
        Displays a list of game results to the user.
        Args:
            results (list): List of result strings to display.
        """
        print("Game Results:")
        for result in results:
            print(result)
    
    def run(self):
        """
        Entry point for running the CLI interface.
        Starts the game, displays the menu, and handles user choices.
        """
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