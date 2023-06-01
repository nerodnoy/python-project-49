import random

RULE = 'What number is missing in the progression?'


def create_progression():
    first_number = random.randint(1, 20)
    progression = [first_number]
    progression_length = random.randint(5, 10)
    gap = random.randint(2, 10)

    while len(progression) <= progression_length:
        next_number = progression[-1] + gap
        progression.append(next_number)

    return progression


def game_conditions():
    progression = create_progression()
    answer = random.choice(progression)

    index = progression.index(answer)
    progression[index] = '..'

    question = ' '.join(map(str, progression))
    correct_answer = str(answer)

    return question, correct_answer
