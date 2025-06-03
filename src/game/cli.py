from .engine import GameEngine

class CLIInterface:
    def __init__(self):
        self.engine = GameEngine()

    def start_game(self):
        print("Welcome to the Game!")
        