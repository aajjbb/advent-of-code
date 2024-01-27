import sys

if __name__ == "__main__":
    x, y = 0, 0

    for line in sys.stdin.readlines():
        command, value = line.split(" ")

        if command == "forward":
            x += int(value)
        elif command == "up":
            y -= int(value)
        elif command == "down":
            y += int(value)
        else:
            print("Broken")
            break

    print(x * y)