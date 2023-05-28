import random

rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    number = random.randint(0, 100)

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return number, correct_answer
