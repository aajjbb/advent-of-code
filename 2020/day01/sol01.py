import sys

values = []
a = 0
b = 0
for line in sys.stdin.readlines():
    val = int(line)

    if 2020 - val in values:
        a = val
        b = 2020 - val
    values.append(val)

print(a * b)