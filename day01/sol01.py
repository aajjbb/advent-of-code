import sys

if __name__ == "__main__":
    calories = []
    buffer = 0

    for line in sys.stdin.readlines():
        if line == "\r\n":
            calories.append(buffer)
            buffer = 0
            continue

        buffer += int(line)

    calories.append(buffer)

    print(max(calories))
