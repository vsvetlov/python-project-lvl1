"""Brain-calc game."""
import random

GAME_RULES = 'What number is missing in the progression?'
GAME_COMPLEXITY = (11, 5, 11)


def create_progression(game_complexity):
    """
    Create random progressions with defined complexity.

    Return progression, missed position

    Args:
        game_complexity: first number, diff, length of progression

    Returns:
        tuple, int
    """
    first_number = random.randrange(game_complexity[0])
    diff = random.randrange(2, game_complexity[1])
    progression_length = random.randrange(6, game_complexity[2])
    missed_position = random.randrange(progression_length)
    progression = ()
    current_number = first_number
    for _ in range(progression_length):
        progression += (str(current_number),)
        current_number += diff
    return progression, missed_position


def make_attempt():
    """
    Define logic of brain-progression game.

    Return correct answer, game's question

    Returns:
        str
    """
    progression, missed_position = create_progression(GAME_COMPLEXITY)
    correct_answer = progression[missed_position]
    progression_for_question = (
        progression[:missed_position]
        + ('..',)
        + progression[missed_position + 1:]
    )
    game_question = 'Question: {0}'.format(' '.join(progression_for_question))
    return game_question, str(correct_answer)
