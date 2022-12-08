""" INST 326 - Object Oriented Programming
# Assignment: Exercise1 - Rock, Paper Scissors
# Navigator: Robin Godinho
# Driver: Wel Mannaseh """

import sys
import argparse
import os


def determine_winner(p1, p2):
    if p1 == p2:
        return "tie"
    elif p1 == "s":
        if p2 == "p":
            return "player1"
        else:
            return "player2"
    elif p1 == "r":
        if p2 == "p":
            return "player2"
        else:
            return "player1"
    elif p1 == "p":
        if p2 == "s":
            return "player2"
        else:
            return "player1"
    else:
        return "err:invalid"
        

def main(player1_name, player2_name):
    nameBoard = {"player1": player1_name, "player2": player2_name}
    # print(nameBoard);
    # os.system('cls||clear')
    p1_input = input("Enter player 1's hand shape ('r', 'p', or 's'):")

    p2_input = input("Enter player 2's hand shape ('r', 'p', or 's'):")

    os.system('cls||clear')

    result = determine_winner(p1_input, p2_input)
    if (result == "tie"):
        print("Tie!")
    elif (result in nameBoard.keys()):
        print(f'{nameBoard[result]} wins!')
    else:
        print(f'Error is: {result}')


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    Args:
    args_list (list) : the list of strings from the command prompt
    Returns:
    args (ArgumentParser)
    """

    # For the sake of readability it is important to insert comments all throughout.
    # Complicated operations get a few lines of comments before the operations commence.
    # Non-obvious ones get comments at the end of the line.
    # For example:
    # This function uses the argparse module in order to parse command line arguments.

    parser = argparse.ArgumentParser()  # Create an ArgumentParser object.

    # Then we will add arguments to this parser object.
    # In this case, we have a required positional argument.
    # Followed by an optional keyword argument which contains a default value.

    parser.add_argument('p1_name', type=str, help="Please enter Player1's Name ")
    parser.add_argument('p2_name', type=str, help="Please enter Player2's Name ")

    args = parser.parse_args(args_list)  # We need to parse the list of command line arguments using this object.

    return args


if __name__ == "__main__":
    # If name == main statements are statements that basically ask:
    # Is the current script being run natively or as a module?
    # It the script is being run as a module, the block of code under this will not be executed.
    # If the script is being run natively, the block of code below this will be executed.
    arguments = parse_args(sys.argv[1:])  # Pass in the list of command line arguments to the parse_args function.
    # print(arguments)

    # The returned object is an object with those command line arguments as attributes of an object.
    # We will pass both of these arguments into the main function.
    # Note that you do not need a main function, but you might find it helpfull.
    # You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.

    main(arguments.p1_name, arguments.p2_name)