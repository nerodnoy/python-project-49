import prompt


max_rounds = 3


def play(game):
    '''The Engine. It greets players and boots games.'''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.rule)

    for _ in range(max_rounds):

        number, correct_answer = game.game_conditions()
        print(f'Question: {number}')
        player_answer = prompt.string('Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
