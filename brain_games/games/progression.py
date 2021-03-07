"""Brain-calc game."""
import random

from brain_games.games.gameplay import play_game

GAME_RULES = 'What number is missing in the progression?'
MAX_ATTEMPTS = 3


def start_game():
    """Initiate gameplay of specific game."""
    play_game(GAME_RULES, MAX_ATTEMPTS, make_attempt_progression)


def create_progression(game_complexity):  # noqa: WPS210
    """
    Create random progressions with defined complexity.

    Return progression, missed number

    Args:
        game_complexity: first number, diff, length of progression

    Returns:
        str, int
    """
    first_number = random.randrange(game_complexity[0])
    diff = random.randrange(2, game_complexity[1])
    progression_length = random.randrange(6, game_complexity[2])
    missed_position = random.randrange(1, progression_length + 1)
    current_position = 1
    progression = ''
    current_number = first_number
    missed_number = 0
    while current_position <= progression_length:
        if missed_position == current_position:
            progression += ' ..'
            missed_number = current_number
        else:
            progression += ' ' + str(current_number)
        current_number += diff
        current_position += 1
    return progression, missed_number


def make_attempt_progression():
    """
    Define logic of brain-progression game.

    Return correct answer, game's question

    Returns:
        str
    """
    game_complexity = (11, 5, 11)
    progression, correct_answer = create_progression(game_complexity)
    game_question = 'Question:{0}'.format(progression)
    return game_question, str(correct_answer)
