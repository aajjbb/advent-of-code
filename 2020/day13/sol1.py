import sys
import math

if __name__ == "__main__":
    earlier_time = int(input())
    bus_times = list(
        map(lambda x: int(x),
            list(filter(lambda x: x != 'x',
                        input().split(',')))))

    wait_time = 10**10
    answer = -1

    for bus_time in bus_times:
        multiplier = int(math.ceil(earlier_time / bus_time))
        earliest_bus_time = multiplier * bus_time

        if wait_time > earliest_bus_time:
            wait_time = earliest_bus_time
            answer = bus_time * (earliest_bus_time - earlier_time)
        # print(bus_time, earliest_bus_time - earlier_time)
        # print(earlier_time, earliest_bus_time)
    print(answer)