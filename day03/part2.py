DIR_X = {'U': -1, 'D': 1, 'L':  0, 'R': 0}
DIR_Y = {'U':  0, 'D': 0, 'L': -1, 'R': 1}

ORIGIN = (0, 0)

def create_wire_map(instructions):
    mapping = {}
    curr_position = ORIGIN
    steps = 0

    for inst in instructions:
        direction = inst[0]
        length = int(inst[1:])


        for _ in range(length):
            new_x = curr_position[0] + DIR_X[direction]
            new_y = curr_position[1] + DIR_Y[direction]

            curr_position = (new_x, new_y)
            steps += 1

            if curr_position not in mapping:
                mapping[curr_position] = steps

    return mapping


if __name__ == "__main__":
    WIRE_1 = list(input().split(","))
    WIRE_2 = list(input().split(","))

    WIRE_1_PATH = create_wire_map(WIRE_1)
    WIRE_2_PATH = create_wire_map(WIRE_2)

    max_dist = 10**100

    for key in WIRE_1_PATH:
        if not key in WIRE_2_PATH:
            continue
        max_dist = min(max_dist, WIRE_1_PATH[key] + WIRE_2_PATH[key])

    print(max_dist)
