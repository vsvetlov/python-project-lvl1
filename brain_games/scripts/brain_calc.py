#!/usr/bin/env python3

"""Initial script."""

from brain_games.cli import welcome_user
from brain_games.games.gameplay import play_game
from brain_games.games.games import do_attempt_calc


def main():
    """Define main code."""
    user_name = welcome_user()
    do_attempt = do_attempt_calc
    game_rules = 'What is the result of the expression?'
    play_game(user_name, do_attempt, game_rules)


if __name__ == '__main__':
    main()
