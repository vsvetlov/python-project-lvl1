"""CLI functions."""

import prompt


def welcome_user(game_rules):
    """
    Ask for user's name and provide the rules of a game.

    Args:
        game_rules: game's rules

    Return user's name

    Returns:
        str
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}\n{1}'.format(user_name, game_rules))
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
