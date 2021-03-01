"""Common gameplay."""
from brain_games.games.games import (  # noqa: F401
    make_attempt_calc,
    make_attempt_even,
)

MAX_ATTEMPTS = 3


def play_game(user_name, make_attempt, game_rules):
    """
    Define main flow of a game.

    Args:
        user_name: user's name
        make_attempt: invokes of a function that defines logic of specific game
        game_rules: game's rules
    """
    print(game_rules)
    attempt = 1
    while attempt <= MAX_ATTEMPTS:
        user_answer, correct_answer = make_attempt()
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.\n"
                "Let's try again, {2}!".format(  # noqa: WPS326
                    user_answer, correct_answer, user_name,
                ),
            )
            break
        attempt += 1
    else:
        print('Congratulations, {0}!'.format(user_name))
