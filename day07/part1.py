import itertools
import sys

SUM = 1
MULT = 2
INPUT = 3
OUTPUT = 4
HALT = 99

POSITION_MODE = 0
IMMEDIATE_MODE = 1

# Additional input_value argument to comply with day07 input.
def run_program(prog, input_value):
    curr_pos = 0

    while True:
        instruction = int(prog[curr_pos])
        opcode = instruction % 100

        mode_a = (instruction // 100) % 10
        mode_b = (instruction // 1000) % 10
        mode_c = (instruction // 10000) % 10

        if mode_c == IMMEDIATE_MODE:
            sys.exit("Immediate mode on a write parameter")

        if opcode == HALT:
            break
        elif opcode == INPUT:
            pos = prog[curr_pos + 1]

            prog[pos] = input_value

            curr_pos += 2
        elif opcode == OUTPUT:
            pos = prog[curr_pos + 1]

            print(prog[pos])

            curr_pos += 2
        else:
            if curr_pos + 3 >= len(prog):
                sys.exit("Invalid position")

            pos_a = prog[curr_pos + 1]
            pos_b = prog[curr_pos + 2]
            pos_result = prog[curr_pos + 3]

            value_a = prog[pos_a] if mode_a == POSITION_MODE else pos_a
            value_b = prog[pos_b] if mode_b == POSITION_MODE else pos_b

            if opcode == SUM:
                prog[pos_result] = value_a + value_b
            elif opcode == MULT:
                prog[pos_result] = value_a * value_b
            else:
                sys.exit("Invalid opcode")

            curr_pos += 4
    return prog

if __name__ == "__main__":
    PROGRAM = str(input())
    PARSED_PROG = list(map(int, PROGRAM.split(",")))

    PHASE_SETTING = [_ for i in range(5)]
    for perm in itertools.permutations(PHASE_SETTING):


    run_program(PARSED_PROG)
