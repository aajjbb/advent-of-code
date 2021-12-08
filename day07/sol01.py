import sys
import math

EPS = 0.00000001

if __name__ == "__main__":
    input = list(map(int, input().split(",")))

    min_cost = math.inf
    min_goal = -1

    l = 1
    h = 1000000000000000

    while abs(l - h) > EPS:
        goal_a = l + (h - l) / 3
        goal_b = h - (h - l) / 3

        s_a = 0
        s_b = 0

        for elem in input:
            s_a += abs(goal_a - elem)
            s_b += abs(goal_b - elem)

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

    print(min_goal, int(min_cost))