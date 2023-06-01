#!/usr/bin/env python3


from brain_games.engine import launch_game
from brain_games.games import calc_game


def main():
    launch_game(calc_game)


if __name__ == '__main__':
    main()
