"""CLI functions."""

import prompt
import random


def welcome_user():
    """Asks user's name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))

def game_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 1
    while attempt < 4:
        print('Question: {0}'.format(random.randint(1, 1000)))
        user_answer = prompt.string('Your answer: ')
        attempt += 1
