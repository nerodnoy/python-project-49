import prompt
# from brain_games.games.calc_game import rule, calc
# from brain_games.games.even_game import rule, is_even
from brain_games.games.gcd_game import rule, gcd

max_rounds = 3


def play(gcd):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(rule)

    for _ in range(max_rounds):

        number, correct_answer = gcd()  # game_conditions
        print(f'Question: {number}')
        player_answer = prompt.string('Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet\'s try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')