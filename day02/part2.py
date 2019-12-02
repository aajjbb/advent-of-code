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
                return []
                # sys.exit("Invalid opcode")

            curr_pos += 4
    return prog

if __name__ == "__main__":
    PROGRAM = str(input())
    PARSED_PROG = list(map(int, PROGRAM.split(",")))

    GOAL_VALUE = 19690720

    for noun in range(1, 100):
        for verb in range(1, 100):
            copy_prog = PARSED_PROG.copy()
            copy_prog[1] = noun
            copy_prog[2] = verb

            final_program = run_program(copy_prog)

            if final_program == []:
                continue

            if final_program[0] == GOAL_VALUE:
                print(100 * noun + verb)
                sys.exit()
