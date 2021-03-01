#!/usr/bin/env python3

"""Initial script."""

from brain_games.cli import welcome_user
from brain_games.games.gameplay import play_game
from brain_games.games.games import make_attempt_progression


def main():
    """Define main code."""
    user_name = welcome_user()
    make_attempt = make_attempt_progression
    game_rules = 'What number is missing in the progression?'
    play_game(user_name, make_attempt, game_rules)


if __name__ == '__main__':
    main()