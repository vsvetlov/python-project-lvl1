#!/usr/bin/env python3

"""Initial script."""

from brain_games.gameplay import play_game
from brain_games.games import gcd


def main():
    """Define main code."""
    game_type = gcd
    play_game(game_type)


if __name__ == '__main__':
    main()
