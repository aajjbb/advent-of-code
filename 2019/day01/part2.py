import sys

def calc(value):
    return value // 3 - 2

def calc_part2(value):
    part_sum = 0

    while True:
        calc_value = calc(value)

        if calc_value <= 0:
            break

        part_sum += calc_value
        value = calc_value

    return part_sum   

if __name__ == "__main__":
    total_sum = 0

    for line in sys.stdin:
        value = int(line)
        
        total_sum += calc_part2(value)
    
    print(total_sum)
