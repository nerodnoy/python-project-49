import random
import math


rule = 'Find the greatest common divisor of given numbers.'


def NOD():

    one = random.randint(1, 100)
    two = random.randint(1, 100)

    number = '{} {}'.format(one, two)

    answer = math.gcd(one, two)
    correct_answer = str(answer)

    return number, correct_answer
