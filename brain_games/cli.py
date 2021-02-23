"""CLI functions."""

import prompt


def welcome_user():
    """
    Ask for user's name.

    Return user's name

    Returns:
        str
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(user_name))
    return user_name
