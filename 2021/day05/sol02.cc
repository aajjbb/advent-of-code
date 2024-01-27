#include <bits/stdc++.h>

using namespace std;

const int MAX_LINES = 5000;

int board[MAX_LINES][MAX_LINES];

int main() {
    string input_buffer;

    while (getline(cin, input_buffer)) {
        int x1, y1, x2, y2;
        sscanf(input_buffer.c_str(), "%d,%d -> %d,%d", &x1, &y1, &x2, &y2);

        // cout << x1 << " " << y1 << " - " << x2 << " " << y2 << "\n";

        if (x1 != x2 && y1 == y2) {
            if (x1 > x2) swap(x1, x2);

            for (int i = x1; i <= x2; i++) {
                board[i][y1] += 1;
            }
        } else if (x1 == x2 && y1 != y2) {
            if (y1 > y2) swap(y1, y2);

            for (int i = y1; i <= y2; i++) {
                board[x1][i] += 1;
            }
        } else {
            assert(abs(x2 - x1) == abs(y2 - y1));
            int diff = abs(x2 - x1);

            for (int i = 0; i <= diff; i++) {
                int nx = x1;
                int ny = y1;

                if (x1 < x2) {
                    nx += i;
                } else {
                    nx -= i;
                }

                if (y1 < y2) {
                    ny += i;
                } else {
                    ny -= i;
                }

                board[nx][ny] += 1;
            }
        }
    }

    int mult_count = 0;

    for (int i = 0; i < MAX_LINES; i++) {
        for (int j = 0; j < MAX_LINES; j++) {
            if (board[i][j] > 1) {
                mult_count += 1;
            }
        }
    }

    cout << mult_count << "\n";

    return 0;
}