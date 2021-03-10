"""Brain-calc game."""
import random

from brain_games.gameplay import play_game

GAME_RULES = 'What is the result of the expression?'
MAX_ATTEMPTS = 3


def start_game():
    """Initiate gameplay of specific game."""
    play_game(GAME_RULES, MAX_ATTEMPTS, make_attempt_calc)


def calc_answer(number1, number2, sign):
    """
    Calculate expression of 2 random numbers.

    Return result of expression

    Args:
        number1: the 1st random number
        number2: the 2nd random number
        sign: operator of expression

    Returns:
        int
    """
    if sign == '+':
        return number1 + number2
    elif sign == '-':
        return number1 - number2
    elif sign == '*':
        return number1 * number2


def make_attempt_calc():
    """
    Define logic of brain-calc game.

    Return correct answer, user's answer

    Returns:
        str
    """
    game_complexity = 100
    number1 = random.randrange(game_complexity)
    number2 = random.randrange(game_complexity)
    sign = random.choice(['+', '-', '*'])
    game_question = 'Question: {0} {1} {2}'.format(number1, sign, number2)
    correct_answer = calc_answer(number1, number2, sign)
    print(correct_answer)
    return game_question, str(correct_answer)
