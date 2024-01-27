import sys
import math

EPS = 0.0000000001

def cost(start, goal):
    dst = abs(start - goal)

    return (dst * (dst + 1)) // 2

def calc_move_cost(items, goal):
    s = 0

    for elem in items:
        s += cost(goal, elem)

    return s

if __name__ == "__main__":
    input = list(map(int, input().split(",")))

    min_cost = math.inf
    min_goal = -1

    l = 1
    h = 100000000000000000

    while abs(l - h) > EPS:
        goal_a = l + (h - l) / 3
        goal_b = h - (h - l) / 3

        s_a = calc_move_cost(input, goal_a)
        s_b = calc_move_cost(input, goal_b)

        # print(goal_a, goal_b, s_a, s_b)

        if min_cost > s_a:
            min_cost = s_a
            min_goal = goal_a

        if min_cost > s_b:
            min_cost = s_b
            min_goal = goal_b

        if s_a > s_b:
            l = goal_a
        else:
            h = goal_b

    print(int(min_goal), calc_move_cost(input, int(min_goal)))