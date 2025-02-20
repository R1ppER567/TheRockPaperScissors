import os
import random
from typing import Final

import msg_consts


OPTIONS: Final = ("rock", "paper", "scissors")
YES_INPUT: Final = frozenset({"yes", "y", "1"})
NO_INPUT: Final = frozenset({"no", "n", "0"})


def clear() -> None:
    """Clears the console screen depending on the OS."""
    os.system("cls" if os.name == "nt" else "clear")


def get_user_option() -> int:
    """Gets the user's option and returns it as an integer.

    Returns:
        int: The user's option.
    """
    while True:
        user_option = input(msg_consts.INPUT_MSG).strip()

        if user_option.isdigit():
            user_option = int(user_option)
        else:
            clear()
            print(msg_consts.INVALID_TYPE_MSG)
            continue

        if user_option in range(len(OPTIONS)):
            return user_option
        clear()
        print(msg_consts.INVALID_RANGE_MSG)


def is_win(user: int, computer: int, total_options: int) -> bool:
    """Determines whether the user's choice beats the computer's choice

    The function uses modular arithmetic to determine if the user's 
    option is the winning move against the computer's option.

    Args:
        user (int): The index of the user's chosen option.
        computer (int): The index of the computer's chosen option.
        total_options (int): The total number of options in the game.

    Returns:
        bool: True if the user wins, False otherwise.
    """
    return (
        (computer - user) % total_options == 
        (total_options - 1) % total_options
    )


def play_game() -> None:
    """Plays a game of rock, paper, scissors.

    The computer randomly selects an option and the user selects an option.
    The result is then displayed.
    """
    computer_option = random.randrange(len(OPTIONS))
    user_option = get_user_option()

    print(msg_consts.INFO_MSG.format(
        OPTIONS[user_option], OPTIONS[computer_option]
    ))

    if user_option == computer_option:
        print(msg_consts.DRAW_MSG)
    elif is_win(user_option, computer_option, len(OPTIONS)):
        print(msg_consts.WIN_MSG)
    else:
        print(msg_consts.LOSE_MSG)


def play_again() -> bool:
    """Asks the user if they want to play again.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    while True:
        play_again = input(msg_consts.PLAY_AGAIN_MSG).strip().lower()

        if play_again in YES_INPUT:
            return True
        if play_again in NO_INPUT:
            return False


def main() -> None:
    """Main function of the program."""
    clear()

    while True:
        play_game()

        if not play_again():
            break

        clear()


if __name__ == "__main__":
    main()
