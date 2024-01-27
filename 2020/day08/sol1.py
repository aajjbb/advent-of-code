import sys

operation_list = []

accumulator = 0
pointer = 0
seen_pointers = set()

if __name__ == "__main__":
    for line in sys.stdin:
        args = line.split(' ')
        operation, value = args[0], int(args[1])

        operation_list.append((operation, value))


    while pointer not in seen_pointers:
        operation, value = operation_list[pointer]
        seen_pointers.add(pointer)

        if operation == 'nop':
            pointer += 1
        elif operation == 'acc':
            accumulator += value
            pointer += 1
        elif operation == 'jmp':
            pointer += value

        pointer = (pointer + len(operation_list)) % len(operation_list)

    print(accumulator)