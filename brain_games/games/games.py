"""Collection of games."""

import random

import prompt

EVEN_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
CALC_RULES = 'What is the result of the expression?'


def do_attempt_calc():  # noqa: WPS210
    """
    Define logic of brain-calc game.

    Return result of attempt, user's answer

    Returns:
        bool, int
    """
    game_complexity = ((1, 50), (1, 10))
    number1 = random.randint(game_complexity[0])
    number2 = random.randint(game_complexity[1])
    sign = random.choice(['+', '-', '*'])
    print('Question: {0} {1} {2}'.format(number1, sign, number2))
    if sign == '+':
        correct_answer = number1 + number2
    elif sign == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    print(correct_answer)
    user_answer = prompt.string('Your answer: ')
    if user_answer.isdecimal():
        user_answer = int(user_answer)
    else:
        return False, user_answer
    return user_answer == correct_answer, user_answer


def do_attempt_even():
    """
    Define logic of brain-even game.

    Return result of attempt, user's answer

    Returns:
        bool, int
    """
    number = random.randint(1, 1000)
    print('Question: {0}'.format(number))
    user_answer = prompt.string('Your answer: ')
    game_move = (user_answer, number % 2)
    if game_move == ('yes', 0) or game_move == ('no', 1):  # noqa: WPS514
        return True, user_answer
    return False, user_answer
