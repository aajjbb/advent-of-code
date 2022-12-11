import sys

if __name__ == "__main__":
    SIZE = 14
    input = sys.stdin.readline().strip()

    for i in range(SIZE, len(input)):
        if len(set(input[i - SIZE:i])) == SIZE:
            print(i)
            break
