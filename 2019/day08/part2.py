WIDTH = 25
HEIGHT = 6

if __name__ == "__main__":
    DIGITS = str(input())

    LAYERS = len(DIGITS) // (WIDTH * HEIGHT)

    curr_digit_pos = 0
    digit_cnt = [[0 for digit in range(10)] for _ in range(LAYERS)]

    color = [[[2 for j in range(WIDTH)] for i in range(HEIGHT)] for _ in range(LAYERS)]
    final_color = [[2 for j in range(WIDTH)] for i in range(HEIGHT)]

    for layer in range(LAYERS):
        for i in range(HEIGHT):
            for j in range(WIDTH):
                curr_digit = int(DIGITS[curr_digit_pos])

                color[layer][i][j] = curr_digit

                curr_digit_pos += 1

    for i in range(HEIGHT):
        for j in range(WIDTH):
            for layer in range(LAYERS):
                if color[layer][i][j] != 2:
                    final_color[i][j] = str(color[layer][i][j])
                    break

        print(''.join(final_color[i]))
