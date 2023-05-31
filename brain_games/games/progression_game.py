import random

rule = 'What number is missing in the progression?'


def progression():

    number_one = random.randint(1, 20)
    line = [number_one]
    size = random.randint(5, 10)
    gap = random.randint(2, 10)

    while len(line) <= size:
        next_number = line[-1] + gap
        line.append(next_number)

    return line


def game_conditions():

    line = progression()
    answer = random.choice(line)

    index = line.index(answer)

    line[index] = '..'

    numbers = ' '.join(map(str, line))
    correct_answer = str(answer)

    return numbers, correct_answer
