import sys

def run_code(operation_list):
    accumulator = 0

    pointer = 0
    seen_pointers = set()

    while 0 <= pointer < len(operation_list):
        if pointer in seen_pointers:
            return (accumulator, False)

        operation, value = operation_list[pointer]
        seen_pointers.add(pointer)

        if operation == 'nop':
            pointer += 1
        elif operation == 'acc':
            accumulator += value
            pointer += 1
        elif operation == 'jmp':
            pointer += value

        # pointer = (pointer + len(operation_list)) % len(operation_list)

    return (accumulator, True)


if __name__ == "__main__":
    operation_list = []

    for line in sys.stdin:
        args = line.split(' ')
        operation, value = args[0], int(args[1])

        operation_list.append((operation, value))

    for i in range(0, len(operation_list)):
        op, value = operation_list[i]

        if op == 'nop':
            operation_list[i] = ('jmp', value)
            acc, valid = run_code(operation_list)

            if valid:
                print(acc)
            operation_list[i] = ('nop', value)
        elif op == 'jmp':
            operation_list[i] = ('nop', value)
            acc, valid = run_code(operation_list)

            if valid:
                print(acc)

            operation_list[i] = ('jmp', value)
