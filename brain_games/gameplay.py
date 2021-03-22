"""Common gameplay."""
from brain_games.cli import ask_user, welcome_user


def play_game(game_type):
    """
    Define main flow of a game and interact with an user.

    Args:
        game_type: contains a function that defines logic of specific game
    """
    user_name = welcome_user()
    print(game_type.GAME_RULES)
    for _ in range(3):
        game_question, correct_answer = game_type.make_attempt()
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
    else:
        print('Congratulations, {0}!'.format(user_name))
