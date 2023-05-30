import random


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True


def game_conditions():

    numbers = random.randint(1, 100)

    if is_prime(numbers) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return numbers, correct_answer
