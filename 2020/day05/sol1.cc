#include <bits/stdc++.h>

using namespace std;

int main() {
    string boarding_pass;
    int highest_seat_id = 0;

    while (cin >> boarding_pass) {
        string row_s = boarding_pass.substr(0, 7);
        string col_s = boarding_pass.substr(7, 3);

        int row = 0;
        int col = 0;

        reverse(row_s.begin(), row_s.end());
        reverse(col_s.begin(), col_s.end());

        for (int i = 0; i < row_s.size(); i++) {
            if (row_s[i] == 'B') {
                row += (1 << i);
            }
        }
        for (int i = 0; i < col_s.size(); i++) {
            if (col_s[i] == 'R') {
                col += (1 << i);
            }
        }

        int seat_id = row * 8 + col;

        highest_seat_id = max(highest_seat_id, seat_id);
    }

    cout << highest_seat_id << endl;
    return 0;
}