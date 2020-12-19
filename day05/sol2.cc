#include <bits/stdc++.h>

using namespace std;

int main() {
    string boarding_pass;
    vector<int> seat_list;

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

        seat_list.push_back(seat_id);
    }

    sort(seat_list.begin(), seat_list.end());
    int my_seat = -1;

    for (int i = 1; i < seat_list.size(); i++) {
        if (seat_list[i] - seat_list[i - 1] == 2) {
            my_seat = seat_list[i] - 1;
            break;
        }
    }

    cout << my_seat << endl;

    return 0;
}