import sys

values = []
a = 0
b = 0
c = 0
for line in sys.stdin.readlines():
    val = int(line)

    for poss_a in values:
        if 2020 - val - poss_a in values:
            a = poss_a
            b = val
            c = 2020 - val - poss_a

    values.append(val)

print(a * b * c)