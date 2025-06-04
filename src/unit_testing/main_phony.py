#from game.cli import CLIInterface
from input_validation import input_valid_check
#from unit_testing.input_validation import input_valid_check


def get_input():
    '''gets input, validates input, returns input'''
    while True:
        x_input = input("\nEnter a value ('a', 'b', 'c', 'd', or 'q' to quit): ")
        a = input_valid_check(x_input)
        if x_input == 'q': exit()
        if a:              return x_input
        else:              print("Invalid entry.  Please try again.")

def main_phoney():
    x = get_input()

    print("x: ", x)


# if __name__ == "__main_phoney__":
main_phoney()