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

def game_value(a, b):
    if is_rock(a):
        if is_paper(b):
            return 0
        elif is_rock(b):
            return 3
        else:
            return 6
    elif is_paper(a):
        if is_scissors(b):
            return 0
        elif is_paper(b):
            return 3
        else:
            return 6
    elif is_scissors(a):
        if is_rock(b):
            return 0
        elif is_scissors(b):
            return 3
        else:
            return 6
    else:
        return -1

if __name__ == "__main__":
    score = 0

    for line in sys.stdin.readlines():
        a, b = line.split()

        score += shape_value(b)
        score += game_value(b, a)

    print(score)