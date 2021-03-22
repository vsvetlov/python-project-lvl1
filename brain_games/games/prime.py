"""Brain-calc game."""
import random

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
GAME_COMPLEXITY = 101


def is_prime(number):
    """
    Calculate if provided number is prime one.

    Return result of calculation

    Args:
        number: a number to test

    Returns:
        bool
    """
    if number == 1:
        return False
    for divider in range(2, number // 2 + 1):
        if number % divider != 0:
            continue
        return False
    return True


def make_attempt():
    """
    Define logic of brain-prime game.

    Return correct answer, game's question

    Returns:
        str
    """
    number = random.randrange(1, GAME_COMPLEXITY)
    game_question = 'Question: {0}'.format(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return game_question, str(correct_answer)
