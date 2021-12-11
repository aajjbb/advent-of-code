import sys

DIR_CNT = 4

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def inside(board, curr_i, curr_j):
    return curr_i >= 0 and curr_i < len(board) and curr_j < len(board[i])

def explore(board, visited, curr_i, curr_j):
    if visited[curr_i][curr_j]:
        return 0

    if board[curr_i][curr_j] == '9':
        return 0

    visited[curr_i][curr_j] = True
    ans = 1

    for k in range(DIR_CNT):
        next_i = curr_i + dx[k]
        next_j = curr_j + dy[k]

        if not inside(board, next_i, next_j):
            continue

        if board[next_i][next_j] <= board[curr_i][curr_j]:
            continue

        ans += explore(board, visited, next_i, next_j)

    return ans


if __name__ == "__main__":
    board = []

    risk_level_sum = 0

    for line in sys.stdin.readlines():
        # Removing the last '\n'
        board.append(str(line)[0:-1])

    visited = [[False for j in range(len(board[i]))] for i in range(len(board))]
    basins = []

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
                basins.append(explore(board, visited, i, j))

    basins = sorted(basins)

    print(basins, basins[-1] * basins[-2] * basins[-3])
