import sys

global_sum = 0
answers = set()

for line in sys.stdin:
    line_content = str(line).replace('\r\n', '')

    if line_content == '':
        global_sum += len(answers)
        answers = set()
        continue

    for char in line_content:
        answers.add(char)

global_sum += len(answers)

print(global_sum)