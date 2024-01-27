import sys

DIR_CNT = 4

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

if __name__ == "__main__":
    board = []

    risk_level_sum = 0

    for line in sys.stdin.readlines():
        # Removing the last '\n'
        board.append(str(line)[0:-1])

    for i in range(len(board)):
        for j in range(len(board[i])):
            smaller_than = 0

            for k in range(DIR_CNT):
                ni = i + dx[k]
                nj = j + dy[k]

                if min(ni, nj) < 0 or ni >= len(board) or nj >= len(board[ni]):
                    continue

                if int(board[ni][nj]) <= int(board[i][j]):
                    smaller_than += 1

            if smaller_than == 0:
                risk_level_sum += int(board[i][j]) + 1

    print(risk_level_sum)
