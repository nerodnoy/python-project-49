import random


rule = 'Find the greatest common divisor of given numbers.'


def gcd():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    numbers = f'{num1} {num2}'

    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    answer = num1 + num2
    correct_answer = str(answer)

    return numbers, correct_answer
