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


def ask_user(game_question):
    """
    Ask an user.

    Args:
        game_question: game's question

    Return user's answer

    Returns:
        str
    """
    print(game_question)
    return prompt.string('Your answer: ')
