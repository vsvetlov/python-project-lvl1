"""Common gameplay."""
from brain_games.cli import ask_user, welcome_user


def play_game(game_rules, max_attempts, game_type):
    """
    Define main flow of a game and interact with an user.

    Args:
        max_attempts: max number of user's moves
        game_type: contains a function that defines logic of specific game
        game_rules: game's rules
    """
    user_name = welcome_user(game_rules)
    attempt = 1
    while attempt <= max_attempts:
        make_attempt = game_type
        game_question, correct_answer = make_attempt()
        user_answer = ask_user(game_question)
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
