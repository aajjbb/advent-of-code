import sys

if __name__ == "__main__":
    input_int = []
    inc = 0

    for line in sys.stdin.readlines():
        input_int.append(int(line))

        if len(input_int) >= 4:
            A = input_int[-4] + input_int[-3] + input_int[-2]
            B = input_int[-3] + input_int[-2] + input_int[-1]

            if A < B:
                inc += 1

    print(inc)