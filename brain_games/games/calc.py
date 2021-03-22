"""Brain-calc game."""
import random

GAME_RULES = 'What is the result of the expression?'
GAME_COMPLEXITY = 100


def calc_answer(number1, number2, sign):
    """
    Calculate expression of 2 random numbers.

    Return result of expression

    Args:
        number1: the 1st random number
        number2: the 2nd random number
        sign: operator of expression

    Raises:
        ValueError: wrong sign

    Returns:
        int
    """
    if sign == '+':
        return number1 + number2
    elif sign == '-':
        return number1 - number2
    elif sign == '*':
        return number1 * number2
    raise ValueError('Incorrect sign')


def make_attempt():
    """
    Define logic of brain-calc game.

    Return correct answer, user's answer

    Returns:
        str
    """
    number1 = random.randrange(GAME_COMPLEXITY)
    number2 = random.randrange(GAME_COMPLEXITY)
    sign = random.choice(['+', '-', '*'])
    game_question = 'Question: {0} {1} {2}'.format(number1, sign, number2)
    correct_answer = calc_answer(number1, number2, sign)
    return game_question, str(correct_answer)
