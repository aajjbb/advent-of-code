import sys

def is_rock(shape):
    if shape == 'A' or shape == 'X':
        return True
    return False

def is_paper(shape):
    if shape == 'B' or shape == 'Y':
        return True
    return False

def is_scissors(shape):
    if shape == 'C' or shape == 'Z':
        return True
    return False

def shape_value(shape):
    if is_rock(shape):
        return 1
    elif is_paper(shape):
        return 2
    elif is_scissors(shape):
        return 3
    else:
        return -1

def game_value(b):
    if is_rock(b):
        return 0
    elif is_paper(b):
        return 3
    elif is_scissors(b):
        return 6
    else:
        return -1

if __name__ == "__main__":
    score = 0
    score_table = {
        "AX": 3 + 0,
        "AY": 1 + 3,
        "AZ": 2 + 6,
        "BX": 1 + 0,
        "BY": 2 + 3,
        "BZ": 3 + 6,
        "CX": 2 + 0,
        "CY": 3 + 3,
        "CZ": 1 + 6,

    }

    for line in sys.stdin.readlines():
        a, b = line.split()

        score += score_table[a+b]

    print(score)