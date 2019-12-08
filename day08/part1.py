WIDTH = 25
HEIGHT = 6

if __name__ == "__main__":
    DIGITS = str(input())

    LAYERS = len(DIGITS) // (WIDTH * HEIGHT)

    curr_digit_pos = 0
    digit_cnt = [[0 for digit in range(10)] for _ in range(LAYERS)]

    print(digit_cnt)

    for layer in range(LAYERS):
        for i in range(HEIGHT):
            for j in range(WIDTH):
                curr_digit = int(DIGITS[curr_digit_pos])

                digit_cnt[layer][curr_digit] += 1

                curr_digit_pos += 1

    answer = 0
    zero_global_min = 10**10

    for layer in range(LAYERS):
        if digit_cnt[layer][0] > zero_global_min:
            continue
        zero_global_min = digit_cnt[layer][0]
        answer = digit_cnt[layer][1] * digit_cnt[layer][2]

    print(answer)
