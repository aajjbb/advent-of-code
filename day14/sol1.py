import re
import sys

BIT_LENGTH = 36


def calc_value(value, mask):
    ret = 0

    mask = mask[::-1]

    for i in range(0, BIT_LENGTH):
        pos = i

        if mask[pos] == '1':
            ret |= (1 << pos)
        elif mask[pos] == 'X':
            if value & (1 << pos) > 0:
                ret |= (1 << pos)

    return ret


if __name__ == "__main__":
    bitmask = ""
    memory = {}

    for line in sys.stdin:
        line_content = line.replace('\r\n', '')

        if line_content.startswith("mask"):
            mask = re.search("mask = (\w*)", line_content).group(1)
        else:
            pos, value = re.search("mem\[(\d*)\] = (\d*)",
                                   line_content).groups()

            memory[pos] = calc_value(int(value), mask)

    print(sum([val for val in memory.values()]))