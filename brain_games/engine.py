import prompt


MAX_ROUNDS = 3


def launch_game(game):
    '''The Engine. It greets players and boots games.'''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.RULE)

    for _ in range(MAX_ROUNDS):

        question, correct_answer = game.game_conditions()
        print(f'Question: {question}')
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
