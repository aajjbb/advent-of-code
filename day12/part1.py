import re
import sys

def total_energy(position, velocity):
    if len(position) != len(velocity):
        sys.exit("Failed to calculate total energy. Mismatch in vectors size")

    energy = 0

    for i in range(len(position)):
        energy += sum(list(map(abs, position[i]))) * sum(list(map(abs, velocity[i])))

    return energy

if __name__ == "__main__":
    DIMENSIONS = 3
    STEPS = 1000

    planet_pos = []

    for line in sys.stdin:
        matches = re.search('<x=(.*), y=(.*), z=(.*)>', line)
        x, y, z = matches.group(1), matches.group(2), matches.group(3)

        planet_pos.append(list(map(int, [x, y, z])))

    PLANETS = len(planet_pos)

    planet_vel = [[0 for dim in range(DIMENSIONS)] for _ in range(PLANETS)]

    for steps in range(STEPS):
        print(planet_pos)
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

    print(total_energy(planet_pos, planet_vel))
