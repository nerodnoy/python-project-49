import prompt 
from brain_games.games.even_game import rule, is_even

max_rounds = 3

def play(is_even):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(rule)

    for _ in range (max_rounds):

        number, correct_answer = is_even()
        print(f'Question: {number}')
        player_answer = prompt.string('Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f'''{player_answer} is wrong answer ;(. Correct answer was {correct_answer}'.
Let's try again, {name}!''') 
            print(f"Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')
