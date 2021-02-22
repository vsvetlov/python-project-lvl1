"""Game's logic."""

import prompt


def welcome_user():
    """Asks user's name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))
