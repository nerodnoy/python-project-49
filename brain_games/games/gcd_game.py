import random


RULE = 'Find the greatest common divisor of given numbers.'


def game_conditions():

    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    question = f'{number1} {number2}'

    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1

    answer = number1 + number2
    correct_answer = str(answer)

    return question, correct_answer
