import sys

def compute_intersection(sets):
    init_set = sets.pop()

    for local_set in sets:
        init_set &= local_set

    return len(init_set)

global_sum = 0
answer_sets = []

for line in sys.stdin:
    line_content = str(line).replace('\r\n', '')

    if line_content == '':
        global_sum += compute_intersection(answer_sets)
        answer_sets = []
        continue

    buffer_set = set()

    for char in line_content:
        buffer_set.add(char)

    answer_sets.append(buffer_set)

global_sum += compute_intersection(answer_sets)

print(global_sum)