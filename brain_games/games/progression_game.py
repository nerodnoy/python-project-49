import random

rule = 'What number is missing in the progression?'


def game_conditions():
    num = random.randint(1, 20)
    gap = random.randint(2, 5)

    line = [num, num + gap, num + (gap * 2), num + (gap * 3), num + (gap * 4), num + (gap * 5), num + (gap * 6), num + (gap * 7), num + (gap * 8), num + (gap * 9), num + (gap * 10)]

    answer = random.choice(line)

    index = line.index(answer)

    line[index] = '..'

    numbers = ' '.join(map(str, line))
    correct_answer = str(answer)

    return numbers, correct_answer
