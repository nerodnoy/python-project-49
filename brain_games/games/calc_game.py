import random


rule = 'What is the result of the expression?'


def calc():

    operand1 = random.randint(1, 20)
    operand2 = random.randint(1, 10)
    operators = ["+", "-", "*"]
    picked_operator = random.choice(operators)

    number = '{} {} {}'.format(operand1, picked_operator, operand2)

    if picked_operator == '+':
        result = operand1 + operand2
    elif picked_operator == '-':
        result = operand1 - operand2
    elif picked_operator == '*':
        result = operand1 * operand2
    correct_answer = str(result)

    return number, correct_answer
