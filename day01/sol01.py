import sys

if __name__ == "__main__":
    input_int = []
    inc = 0

    for line in sys.stdin.readlines():
        input_int.append(int(line))

        if len(input_int) > 1 and input_int[-1] > input_int[-2]:
            inc += 1

    print(inc)