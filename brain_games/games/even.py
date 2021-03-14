"""Brain-calc game."""
import random

from brain_games.gameplay import play_game

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_ATTEMPTS = 3
GAME_COMPLEXITY = 1000


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
    number = random.randrange(GAME_COMPLEXITY)
    game_question = 'Question: {0}'.format(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return game_question, correct_answer
