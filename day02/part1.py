import sys

SUM = 1
MULT = 2
HALT = 99

def run_program(prog):
    curr_pos = 0

    while True:
        if prog[curr_pos] == HALT:
            break
        else:
            if curr_pos + 3 >= len(prog):
                sys.exit("Invalid position")

            pos_a = prog[curr_pos + 1]
            pos_b = prog[curr_pos + 2]
            pos_result = prog[curr_pos + 3]

            value_a = prog[pos_a]
            value_b = prog[pos_b]

            if prog[curr_pos] == SUM:
                prog[pos_result] = value_a + value_b
            elif prog[curr_pos] == MULT:
                prog[pos_result] = value_a * value_b
            else:
                sys.exit("Invalid opcode")

            curr_pos += 4
    return prog

if __name__ == "__main__":
    PROGRAM = str(input())
    PARSED_PROG = list(map(int, PROGRAM.split(",")))

    PARSED_PROG[1] = 12
    PARSED_PROG[2] = 2

    FINAL_PROGRAM = run_program(PARSED_PROG)

    print(FINAL_PROGRAM[0])
