"""Collection of gameplay functions."""

import random

import prompt


def game_even(user_name):
    """
    Describe gameplay of brain-even.

    Args:
        user_name: user's name
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 1
    while attempt < 4:
        number = random.randint(1, 1000)
        print('Question: {0}'.format(number))
        user_answer = prompt.string('Your answer: ')
        user_move = (user_answer, number % 2)
        if user_move == ('yes', 0) or user_move == ('no', 1):  # noqa: WPS514
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer. Let's try again, {1}!".format(
                    user_answer, user_name))
            break
        attempt += 1
    else:
        print('Congratulations, {0}!'.format(user_name))
