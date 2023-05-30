import random


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_conditions():

    numbers = random.randint(3, 100)

    divider = 2

    while divider <= numbers / 2:
        if numbers % divider == 0:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'
        divider += 1

    return numbers, correct_answer
