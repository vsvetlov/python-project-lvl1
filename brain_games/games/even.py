"""Brain-calc game."""
import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_RANDOM_NUMBER = 1000


def make_attempt():
    """
    Define logic of brain-even game.

    Return game's question, correct answer

    Returns:
        str, bool
    """
    number = random.randrange(MAX_RANDOM_NUMBER)
    game_question = 'Question: {0}'.format(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return game_question, correct_answer
