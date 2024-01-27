#include <bits/stdc++.h>

using namespace std;

int visiblePoints(vector<vector<int>> board) {
    int ans = 0;

    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            if (board[i][j] > 0) {
                ans += 1;
            }
        }
    }

    return ans;
}

vector<vector<int> > fold_x(vector<vector<int>> board, int axis) {
    vector<vector<int>> return_board(board.size(), vector<int>(axis));

    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < axis; j++) {
            return_board[i][j] = board[i][j];
        }
    }

    for (int j = axis + 1, new_idx = axis - 1; j < board[0].size() && new_idx >= 0; j++, new_idx--) {
        for (int i = 0; i < board.size(); i++) {
            return_board[i][new_idx] += board[i][j];
        }
    }

    return return_board;
}

vector<vector<int> > fold_y(vector<vector<int>> board, int axis) {
    vector<vector<int>> return_board(axis, vector<int>(board[0].size()));

    for (int i = 0; i < axis; i++) {
        for (int j = 0; j < board[i].size(); j++) {
            return_board[i][j] = board[i][j];
        }
    }
    for (int i = axis + 1, new_idx = axis - 1; i < board.size() && new_idx >= 0; i++, new_idx--) {
        for (int j = 0; j < board[0].size(); j++) {
            return_board[new_idx][j] += board[i][j];
        }
    }

    return return_board;
}

int main() {
    int x_cord, y_cord;

    vector<pair<int, int>> points;
    int max_x = 0;
    int max_y = 0;

    while (scanf("%d,%d", &x_cord, &y_cord) == 2) {
        points.push_back(make_pair(x_cord, y_cord));
        max_x = max(max_x, x_cord);
        max_y = max(max_y, y_cord);
    }

    vector<vector<int>> board(max_y + 1, vector<int>(max_x + 1, 0));

    for (int i = 0; i < points.size(); i++) {
        board[points[i].second][points[i].first] = 1;
    }

    char axis;
    int sep;

    int folds = 0;

    while (scanf("fold along %c=%d\n", &axis, &sep) == 2) {
        if (axis == 'x') {
            board = fold_x(board, sep);
        } else if (axis == 'y') {
            board = fold_y(board, sep);
        }
        // for (int i = 0; i < board.size(); i++) {
        //     for (int j = 0; j < board[i].size(); j++) {
        //         cout << board[i][j] << " ";
        //     }
        //     cout << endl;
        // }

        folds += 1;

        if (folds == 1) {
            break;
        }
    }

    printf("%d\n", visiblePoints(board));

    return 0;
}