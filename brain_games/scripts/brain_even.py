#!/usr/bin/env python3

"""Initial script."""

from brain_games.cli import welcome_user
from brain_games.games.gameplay import play_game
from brain_games.games.games import make_attempt_even


def main():
    """Define main code."""
    user_name = welcome_user()
    make_attempt = make_attempt_even
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(user_name, make_attempt, game_rules)


if __name__ == '__main__':
    main()
