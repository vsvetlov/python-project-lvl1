"""Brain-calc game."""
import random

from brain_games.gameplay import play_game

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_ATTEMPTS = 3


def start_game():
    """Initiate gameplay of specific game."""
    play_game(GAME_RULES, MAX_ATTEMPTS, make_attempt_even)


def make_attempt_even():
    """
    Define logic of brain-even game.

    Return game's question, correct answer

    Returns:
        str, bool
    """
    game_complexity = 1000
    number = random.randrange(game_complexity)
    game_question = 'Question: {0}'.format(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return game_question, correct_answer
