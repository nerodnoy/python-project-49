#!/usr/bin/env python3


from brain_games.engine import launch_game
from brain_games.games import progression_game


def main():
    launch_game(progression_game)


if __name__ == '__main__':
    main()
