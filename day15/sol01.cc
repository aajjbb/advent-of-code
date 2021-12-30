#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1010;
const int INF = INT_MAX / 4;

int dp[MAXN][MAXN];

int func(int r, int c, const vector<string>& field) {
    if (r >= field.size() || c >= field[r].size()) {
        return INF;
    } else if (r == field.size() - 1 && c == field[r].size() - 1) {
        return field[r][c] - '0';
    } else {
        int& ans = dp[r][c];

        if (ans == -1) {
            ans = INF;

            int cost = field[r][c] - '0';

            ans = min(ans, cost + func(r + 1, c, field));
            ans = min(ans, cost + func(r, c + 1, field));
        }

        return ans;
    }
}

int main() {
    memset(dp, -1, sizeof(dp));

    vector<string> field;
    string input_s;

    while (cin >> input_s) {
        field.push_back(input_s);
    }

    cout << func(0, 0, field) - (field[0][0] - '0') << "\n";

    return 0;
}