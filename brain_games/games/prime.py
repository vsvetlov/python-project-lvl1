"""Brain-calc game."""
import random

from brain_games.games.gameplay import play_game

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_ATTEMPTS = 3


def start_game():
    """Initiate gameplay of specific game."""
    play_game(GAME_RULES, MAX_ATTEMPTS, make_attempt_prime)


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


def make_attempt_prime():
    """
    Define logic of brain-prime game.

    Return correct answer, game's question

    Returns:
        str
    """
    game_complexity = 101
    number = random.randrange(1, game_complexity)
    game_question = 'Question: {0}'.format(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return game_question, str(correct_answer)
