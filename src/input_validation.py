def input_validation(x_input):
    '''This function takes input and checks that it is 1 character and a correct choice.
    Next it returns True. Otherwise an error is printed and False is returned.
    To test - uncomment "Testing code:" and the following lines.'''

    # Use 'try' to catch all exceptions
    try:
        # Make input lowercase - and checks if alpha
        x_input = x_input.lower()
        print("x_input: ", x_input)

        # Must be correct input    
        if ((x_input != "a") and (x_input != "b") and (x_input != "c") and (x_input != "d")):
            print("Error: Invalid Entry.  \nPlease enter a, b, c, d (or 'q' to quit): ")
            return False
        
    # All other entries produce error
    except:
        print("Error at except in input validation.")

    # Correct entries return True
    else:

        # If 'q' exit
        if (x_input == "q"): exit()

        # Entry is valid and not 'q'
        return True
    

# # Testing code:
#     # While designing code: Print validation executed.
#     finally:
#         print("input_validation() completed.")

# # Testing:
# print("Running input_validation.")
# while True:
#     a = input_validation( input("\nEnter a value: "))
#     print("Returning :", a)
#     if a == True: break