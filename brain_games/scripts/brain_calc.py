#!/usr/bin/env python3


from brain_games.engine import play
from brain_games.games import calc_game


def main():
    play(calc_game)


if __name__ == '__main__':
    main()
