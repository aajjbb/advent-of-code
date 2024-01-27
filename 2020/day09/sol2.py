import sys

WINDOW_SIZE = 25
GOAL_VALUE = 1930745883

if __name__ == "__main__":
    input = [int(line) for line in sys.stdin]

    a, b = 0, 1
    global_sum = input[a]

    while b < len(input):
        global_sum += input[b]

        while global_sum > GOAL_VALUE and a < b - 1:
            global_sum -= input[a]
            a += 1

        if global_sum == GOAL_VALUE and b - a > 1:
            print(sum(input[a:b+1]))
            print(min(input[a:b+1]) + max(input[a:b+1]))

        b += 1
