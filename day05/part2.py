import sys

SUM = 1
MULT = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
HALT = 99

POSITION_MODE = 0
IMMEDIATE_MODE = 1

def run_program(prog):
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
            # Adhering to the problem statement, the input must be "1"
            pos = prog[curr_pos + 1]

            prog[pos] = 5

            curr_pos += 2
        elif opcode == OUTPUT:
            pos = prog[curr_pos + 1]

            print(prog[pos])

            curr_pos += 2
        elif opcode == JUMP_IF_TRUE:
            pos_a = prog[curr_pos + 1]
            pos_b = prog[curr_pos + 2]

            value_a = prog[pos_a] if mode_a == POSITION_MODE else pos_a
            value_b = prog[pos_b] if mode_b == POSITION_MODE else pos_b

            if value_a != 0:
                curr_pos = value_b
            else:
                curr_pos += 3
        elif opcode == JUMP_IF_FALSE:
            pos_a = prog[curr_pos + 1]
            pos_b = prog[curr_pos + 2]

            value_a = prog[pos_a] if mode_a == POSITION_MODE else pos_a
            value_b = prog[pos_b] if mode_b == POSITION_MODE else pos_b

            if value_a == 0:
                curr_pos = value_b
            else:
                curr_pos += 3
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
            elif opcode == LESS_THAN:
                prog[pos_result] = 1 if value_a < value_b else 0
            elif opcode == EQUALS:
                prog[pos_result] = 1 if value_a == value_b else 0
            else:
                sys.exit("Invalid opcode")

            curr_pos += 4
    return prog

if __name__ == "__main__":
    PROGRAM = str(input())
    PARSED_PROG = list(map(int, PROGRAM.split(",")))

    run_program(PARSED_PROG)
