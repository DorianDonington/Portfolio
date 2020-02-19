#NIA's: 217447, 217723, 194985. Group Code: AN. Professor: Sergio Ivan Giraldo 

from hanoi.hanoi import HanoiGame
from hanoi.hanoi_exception import HanoiException

def get_int_value(message, range_start, range_end):
    """
    Sends the user the input message and checks that the input data is an integer between range_start and range_end.
    Returns the value if is correct, None otherwise.

    :param message: Message for the user asking for some integer input
    :param range_start: First value into the valid range.
    :param range_end: First value out of the valid range.
    :return: the number or nothing
    """

    value = None
    while value is None:
        value = input(message)
        try:
            value = int(value)
            if value < range_start or value > range_end:
                print("The value should be between %d and %d! Try again." % (range_start, range_end))
                value = None
        except ValueError:
            value = None
            print("This is not a valid input value! Try again.")
        
    return value

def do_move(hanoi_game):
    """
    Asks the user for a move and returns True if the move lead to a finishing state.

    :param hanoi_game: The game instance the program is using.
    :return: True if the move reached a finishing state, False otherwise.
    """

    done = False
    while not done:
    
        try:
            source_tower = get_int_value("Move from? (tower 1, 2 or 3, 0 to cancel)\n", 0, 3)
            if source_tower:
                target_tower = get_int_value("Move to? (tower 1, 2 or 3, 0 to cancel)\n", 0, 3)

                if target_tower:
                    hanoi_game.move(source_tower-1, target_tower-1)
                else:
                    print("Move canceled!")
            else:
                print("Move canceled!")
            done = True

        except HanoiException as exc:
            print(exc)
            print()

    return hanoi_game.is_finished()


game_options = """
What do you want to do?
    1.- Do a move
    2.- Show current state
    3.- Show optimal solution
    4.- Restart the game
    5.- Show hint
    0.- Quit"""


def play_game():
    """
    Main loop for interactive play.
    """

    n_discs = get_int_value("How many discs do you want?\n",1,15) #De 3 a 10?
    hanoi_game = HanoiGame(n_discs)

    print(hanoi_game)

    quit_game = False

    while not quit_game:
        print(game_options)

        selected_option = input()
        if selected_option == "0":
            quit_game = True

        elif selected_option == "1":
            do_move(hanoi_game)
            print("\nCurrent state:")
            print(hanoi_game)
            quit_game = hanoi_game.is_finished()

        elif selected_option == "2":
            print("\nCurrent state:")
            print(hanoi_game)

        elif selected_option == "3":
            hanoi_game.print_optimal_solution()
        
        elif selected_option == "4":
            print("Game restarted")
            hanoi_game.start_game()
            print(hanoi_game)

        elif selected_option == "5":
            print(hanoi_game)
            if hanoi_game.pistas() != False:
                print("You should move a disk to the tower number %s" % (hanoi_game.pistas()))
            else:
                print("Oops.. You have done a misstep!")
        else:
            print("This is not a valid option! Let's try again...")

    if hanoi_game.is_finished():
        print("CONGRATS")


header = """
    ################################
    ####### TOWERS OF HANOI ########
    ################################"""

main_options = """
What do you want to do?
    1.- Play hanoi towers!
    2.- Show help
    0.- Exit"""

main_help = """
HOW TO PLAY:

The objective of the game is to move the entire stack of discs from Tower 1 to Tower 3!
But there are two restrictions:
    1) You can move only one disk at a time.
    2) No disk can be placed on top of a smaller disc."""


def show_menu():
    """
    Main loop for the main menu
    """

    print(header)

    exit_game = False
    while not exit_game:
        print(main_options)

        selected_option = input()
        if selected_option == "0":
            exit_game = True

        elif selected_option == "1":
            play_game()

        elif selected_option == "2":
            print(main_help)

        else:
            print("This is not a valid option! Let's try again...")


if __name__ == '__main__':
    show_menu()
