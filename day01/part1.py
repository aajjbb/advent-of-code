import sys

def calc(value):
    return value // 3 - 2

if __name__ == "__main__":
    total_sum = 0

    for line in sys.stdin:
        value = int(line)
        
        total_sum += calc(value)
    
    print(total_sum)
