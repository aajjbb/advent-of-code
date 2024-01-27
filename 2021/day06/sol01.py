import sys

DAYS = 80
LIFETIME = 9

if __name__ == "__main__":
    input = list(map(int, input().split(",")))

    day_cnt = { i : 0 for i in range(LIFETIME) }

    for fish in input:
        if fish in day_cnt:
            day_cnt[fish] += 1
        else:
            day_cnt[fish] = 1

    for _ in range(DAYS):
        new_days = { i : 0 for i in range(LIFETIME) }

        for i in range(0, LIFETIME):
            if i in day_cnt:
                new_days[i - 1] = day_cnt[i]
            else:
                new_days[i - 1] = 0


        new_days[8] += new_days[-1]
        new_days[6] += new_days[-1]
        new_days[-1] = 0

        day_cnt = new_days

    sum = 0

    for i in range(LIFETIME):
        sum += day_cnt[i]
    print(sum)