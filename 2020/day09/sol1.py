import sys

WINDOW_SIZE = 25

if __name__ == "__main__":
    input = [int(line) for line in sys.stdin]

    for i in range(WINDOW_SIZE, len(input)):
        valid = False

        for a in range(i - WINDOW_SIZE, i):
            for b in range(a + 1, i):
                if input[a] + input[b] == input[i]:
                    valid = True
                    break

        if not valid:
            print(input[i])
