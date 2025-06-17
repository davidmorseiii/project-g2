import pytest
import sys
import os

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
game_dir = parent_dir + "\\game"
print("game_dir: ", game_dir)

# Add parent directory to sys.path
sys.path.append(parent_dir)

# Add game directory to sys.path
sys.path.append(game_dir)
import main

# Run tests:
def test_main():
    pass
def test_cli():
    pass
def test_curses_cli():
    pass
def test_game_engine():
    pass
def test_Question():
    pass
