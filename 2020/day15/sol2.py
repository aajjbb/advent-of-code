
GOAL = 30000000

if __name__ == "__main__":
    input = [12,20,0,6,1,17,7]
    last = input[-1]
    memory = {}

    for i in range(len(input)):
        memory[input[i]] = [i + 1]

    for i in range(len(input) + 1, GOAL + 1):
        if len(memory[last]) == 1:
            last = 0

            if 0 in memory:
                memory[0].append(i)
            else:
                memory[0] = [i]
        else:
            last_pos = memory[last][-1]
            before_last_pos = memory[last][-2]

            new_value = last_pos - before_last_pos

            last = new_value

            if new_value in memory:
                memory[new_value].append(i)
            else:
                memory[new_value] = [i]

    print(last)
