"""Collection of games."""
import math
import random

import prompt


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
    print('Question: {0} {1} {2}'.format(number1, sign, number2))
    correct_answer = calc_answer(number1, number2, sign)
    print(correct_answer)
    user_answer = prompt.string('Your answer: ')
    return user_answer, str(correct_answer)


def is_even(number):
    """
    Calculate if provided number is even one.

    Return result in yes/no format

    Args:
        number: a number to test

    Returns:
        str
    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def make_attempt_even():
    """
    Define logic of brain-even game.

    Return correct answer, user's answer

    Returns:
        str
    """
    game_complexity = 1000
    number = random.randrange(game_complexity)
    print('Question: {0}'.format(number))
    user_answer = prompt.string('Your answer: ')
    correct_answer = is_even(number)
    return user_answer, correct_answer


def make_attempt_gcd():
    """
    Define logic of brain-gcd game.

    Return correct answer, user's answer

    Returns:
        str
    """
    game_complexity = 500
    number1 = random.randrange(1, game_complexity)
    number2 = random.randrange(1, game_complexity)
    print('Question: {0} {1}'.format(number1, number2))
    correct_answer = math.gcd(number1, number2)
    print(correct_answer)
    user_answer = prompt.string('Your answer: ')
    return user_answer, str(correct_answer)


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
    progression_length = random.randrange(5, game_complexity[2])
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

    Return correct answer, user's answer

    Returns:
        str
    """
    game_complexity = (11, 5, 11)
    progression, correct_answer = create_progression(game_complexity)
    print('Question: {0}'.format(progression))
    user_answer = prompt.string('Your answer: ')
    return user_answer, str(correct_answer)


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


def make_attempt_prime():
    """
    Define logic of brain-prime game.

    Return correct answer, user's answer

    Returns:
        str
    """
    game_complexity = 101
    number = random.randrange(1, game_complexity)
    print('Question: {0}'.format(number))
    user_answer = prompt.string('Your answer: ')
    correct_answer = is_prime(number)
    return user_answer, str(correct_answer)
