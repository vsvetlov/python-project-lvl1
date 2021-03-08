"""Brain-calc game."""
import math
import random

from brain_games.games.gameplay import play_game

GAME_RULES = 'Find the greatest common divisor of given numbers'
MAX_ATTEMPTS = 3


def start_game():
    """Initiate gameplay of specific game."""
    play_game(GAME_RULES, MAX_ATTEMPTS, make_attempt_gcd)


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
    min_number = number1 if number1 <= number2 else number2
    for divider in range(min_number, 0, -1):
        if number1 % divider == 0 and number2 % divider == 0:
            return divider


def make_attempt_gcd():
    """
    Define logic of brain-gcd game.

    Return correct answer, game's question

    Returns:
        str
    """
    game_complexity = 500
    number1 = random.randrange(1, game_complexity)
    number2 = random.randrange(1, game_complexity)
    game_question = 'Question: {0} {1}'.format(number1, number2)
    correct_answer = calc_gcd(number1, number2)
    print(math.gcd(number1, number2))
    return game_question, str(correct_answer)
