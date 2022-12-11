import sys

if __name__ == "__main__":
    input = sys.stdin.readline().strip()

    for i in range(4, len(input)):
        if len(set(input[i - 4:i])) == 4:
            print(i)
            break
