import re
import sys

BIT_LENGTH = 36


def get_all_index_helper(value, mask):
    mask = mask[::-1]

    return get_all_index(value, mask, 0)

def get_all_index(value, mask, pos):
    if pos >= BIT_LENGTH:
        return set([value])

    value_list = set()

    if mask[pos] == '1':
        value_list |= get_all_index(value | (1 << pos), mask, pos + 1)
    elif mask[pos] == 'X':
        value_list |= get_all_index(value | (1 << pos), mask, pos + 1)
        value_list |= get_all_index(value & ~(1 << pos), mask, pos + 1)
    else:
        value_list |= get_all_index(value, mask, pos + 1)

    return value_list

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

            positions = get_all_index_helper(int(pos), mask)

            for pos in positions:
                memory[pos] = int(value)

    print(sum([val for val in memory.values()]))