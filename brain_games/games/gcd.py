"""Brain-calc game."""
import random

GAME_RULES = 'Find the greatest common divisor of given numbers'
MAX_RANDOM_NUMBER = 500


def calc_gcd(number1, number2):
    """
    Calculate gcd of provided numbers.

    Return gcd

    Args:
        number1: a number to test
        number2: a number to test

    Returns:
        int
    """
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 + number2


def make_attempt():
    """
    Define logic of brain-gcd game.

    Return correct answer, game's question

    Returns:
        str
    """
    number1 = random.randrange(1, MAX_RANDOM_NUMBER)
    number2 = random.randrange(1, MAX_RANDOM_NUMBER)
    game_question = 'Question: {0} {1}'.format(number1, number2)
    correct_answer = calc_gcd(number1, number2)
    return game_question, str(correct_answer)
