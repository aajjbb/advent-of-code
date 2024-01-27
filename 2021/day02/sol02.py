import sys

if __name__ == "__main__":
    x, y = 0, 0
    aim = 0

    for line in sys.stdin.readlines():
        command, value = line.split(" ")

        if command == "forward":
            x += int(value)
            y += aim * int(value)
        elif command == "up":
            aim -= int(value)
        elif command == "down":
            aim += int(value)
        else:
            print("Broken")
            break

    print(x * y)