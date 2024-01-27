import math
import re
import sys

def lcm(a, b):
    return a * b // math.gcd(a, b)

if __name__ == "__main__":
    DIMENSIONS = 3

    planet_position = []

    for line in sys.stdin:
        matches = re.search('<x=(.*), y=(.*), z=(.*)>', line)
        x, y, z = matches.group(1), matches.group(2), matches.group(3)

        planet_position.append(list(map(int, [x, y, z])))

    PLANETS = len(planet_position)

    dimension_steps = []

    for current_dim in range(DIMENSIONS):
        steps = 0
        state_map = {}

        planet_pos = planet_position.copy()
        planet_vel = [[0 for dim in range(DIMENSIONS)] for _ in range(PLANETS)]

        while True:
            gravity = [[0 for dim in range(DIMENSIONS)] for _ in range(PLANETS)]

            for i in range(PLANETS):
                for j in range(PLANETS):
                    for dim in range(DIMENSIONS):
                        if planet_pos[i][dim] > planet_pos[j][dim]:
                            gravity[i][dim] -= 1
                        elif planet_pos[i][dim] < planet_pos[j][dim]:
                            gravity[i][dim] += 1

            for i in range(PLANETS):
                for dim in range(DIMENSIONS):
                    planet_vel[i][dim] += gravity[i][dim]
                    planet_pos[i][dim] += planet_vel[i][dim]

            test_dim = []
            test_vel = []

            for i in range(PLANETS):
                test_dim.append(planet_pos[i][current_dim])
                test_vel.append(planet_vel[i][current_dim])

            current_state = (str(test_dim), str(test_vel))

            if current_state in state_map and max(test_vel) == 0 and min(test_vel) == 0:
                print(current_state, steps)
                dimension_steps.append(steps)
                break
            state_map[current_state] = True
            steps += 1

    meeting_point = 1

    for step in dimension_steps:
        meeting_point = lcm(meeting_point, step)

    print(meeting_point)

