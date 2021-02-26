"""Common gameplay."""
from brain_games.games.games import (  # noqa: F401
    do_attempt_calc,
    do_attempt_even,
)

MAX_ATTEMPTS = 3


def play_game(user_name, do_attempt, game_rules):
    """
    Define main flow of a game.

    Args:
        user_name: user's name
        do_attempt: name of the function that defines logic of specific game
        game_rules: game's rules
    """
    print(game_rules)
    attempt = 1
    while attempt <= MAX_ATTEMPTS:
        attempt_result, user_answer = do_attempt()
        if attempt_result:
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer. Let's try again, {1}!".format(
                    user_answer, user_name,
                ),
            )
            break
        attempt += 1
    else:
        print('Congratulations, {0}!'.format(user_name))
