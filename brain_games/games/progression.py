"""Brain-calc game."""
import random

GAME_RULES = 'What number is missing in the progression?'
GAME_COMPLEXITY = (11, 5, 11)


def create_progression(first_number, diff, progression_length):
    """
    Create random progressions with defined complexity.

    Return progression, missed position

    Args:
        first_number: first number of progression
        diff: diff between progression positions
        progression_length: number of positions

    Returns:
        list
    """
    progression = []
    last_number = first_number + progression_length * diff
    for current_number in range(first_number, last_number, diff):  # noqa:WPS519
        progression.append(str(current_number))
    return progression


def make_attempt():
    """
    Define logic of brain-progression game.

    Return correct answer, game's question

    Returns:
        str
    """
    first_number = random.randrange(GAME_COMPLEXITY[0])
    diff = random.randrange(2, GAME_COMPLEXITY[1])
    progression_length = random.randrange(6, GAME_COMPLEXITY[2])
    missed_position = random.randrange(progression_length)
    progression = create_progression(first_number, diff, progression_length)
    correct_answer = progression[missed_position]
    progression[missed_position] = '..'
    game_question = 'Question: {0}'.format(' '.join(progression))
    return game_question, str(correct_answer)
