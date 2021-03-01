"""Collection of games."""
import math
import random

import prompt


def do_attempt_calc():  # noqa: WPS210
    """
    Define logic of brain-calc game.

    Return result of attempt, user's answer

    Returns:
        bool, int
    """
    game_complexity = 100
    number1 = random.randrange(game_complexity)
    number2 = random.randrange(game_complexity)
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
    if user_answer.lstrip('-').isdecimal():
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
    game_complexity = 1000
    number = random.randrange(game_complexity)
    print('Question: {0}'.format(number))
    user_answer = prompt.string('Your answer: ')
    game_move = (user_answer, number % 2)
    if game_move == ('yes', 0) or game_move == ('no', 1):  # noqa: WPS514
        return True, user_answer
    return False, user_answer


def do_attempt_gcd():
    """
    Define logic of brain-gcd game.

    Return result of attempt, user's answer

    Returns:
        bool, int
    """
    game_complexity = 500
    number1 = random.randint(1, game_complexity)
    number2 = random.randint(1, game_complexity)
    print('Question: {0} {1}'.format(number1, number2))
    correct_answer = math.gcd(number1, number2)
    print(correct_answer)
    user_answer = prompt.string('Your answer: ')
    if user_answer.lstrip('-').isdecimal():
        user_answer = int(user_answer)
        return user_answer == correct_answer, user_answer
    return False, user_answer


def do_attempt_progression():  # noqa: WPS210
    """
    Define logic of brain-progression game.

    Return result of attempt, user's answer

    Returns:
        bool, int
    """
    game_complexity = (11, 5, 11)
    first_number = random.randrange(game_complexity[0])
    diff = random.randrange(2, game_complexity[1])
    progression_length = random.randrange(5, game_complexity[2])
    missed_position = random.randrange(1, progression_length + 1)
    current_position = 1
    progression = ''
    current_number = first_number
    correct_answer = 1
    while current_position <= progression_length:
        if missed_position == current_position:
            progression += ' ..'
            correct_answer = current_number
        else:
            progression += ' ' + str(current_number)
        current_number += diff
        current_position += 1
    print('Question: {0}'.format(progression))
    user_answer = prompt.string('Your answer: ')
    if user_answer.isdecimal():
        user_answer = int(user_answer)
    else:
        return False, user_answer
    return user_answer == correct_answer, user_answer


def is_prime(number):
    """
    Calculate if provided number is prime one.

    Return result in yes/no format

    Args:
        number: a number to test

    Returns:
        str
    """
    divider = 2
    if number <= 3:
        return 'yes'
    while divider < number:
        if number % divider > 0:
            divider += 1
        else:
            return 'no'
    return 'yes'


def do_attempt_prime():
    """
    Define logic of brain-prime game.

    Return result of attempt, user's answer

    Returns:
        bool, int
    """
    game_complexity = 101
    number = random.randrange(1, game_complexity)
    print('Question: {0}'.format(number))
    user_answer = prompt.string('Your answer: ')
    correct_answer = is_prime(number)
    if user_answer == correct_answer:
        return True, user_answer
    return False, user_answer
