#!/usr/bin/env python3

"""Initial script."""

from brain_games.cli import welcome_user
from brain_games.gameplay import game_even


def main():
    """Define main code."""
    user_name = welcome_user()
    game_even(user_name)


if __name__ == '__main__':
    main()
