#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1010;
const int MULT = 4; // How many times the board is expanded.
const int INF = 101010;

int dp[MAXN][MAXN];

int next_value(int value) {
    if (value > 9) {
        return 1 + (value % 10);
    } else {
        return value;
    }
}

int main() {
    memset(dp, 63, sizeof(dp));

    vector<vector<int> > field;
    string input_s;

    while (cin >> input_s) {
        vector<int> row;

        for (int i = 0; i < input_s.size(); i++) {
            row.push_back(input_s[i] - '0');
        }
        field.push_back(row);
    }

    const int size = field.size();

    // add new rows
    for (int s = 1; s <= MULT; s++) {
        for (int i = 0; i < size; i++) {
            vector<int> curr_row = field[i];

            for (int j = 0; j < size; j++) {
                curr_row[j] = next_value(curr_row[j] + s);
            }

            field.push_back(curr_row);
        }
    }

    // add new columns
    for (int i = 0; i < field.size(); i++) {
        for (int s = 1; s <= MULT; s++) {
            for (int j = 0; j < size; j++) {
                field[i].push_back(next_value(field[i][j] + s));
            }
        }
    }

    priority_queue<pair<int, pair<int, int> > > q;
    q.push(make_pair(0, make_pair(0, 0)));

    while (!q.empty()) {
        int curr_cost = -q.top().first;
        int cr = q.top().second.first;
        int cc = q.top().second.second;
        q.pop();

        if (cr + 1 < field.size()) {
            int new_cost = curr_cost + field[cr + 1][cc];

            if (dp[cr + 1][cc] > new_cost) {
                dp[cr + 1][cc] = new_cost;
                q.push(make_pair(-new_cost, make_pair(cr + 1, cc)));
            }
        }
        if (cr - 1 >= 0) {
            int new_cost = curr_cost + field[cr - 1][cc];

            if (dp[cr - 1][cc] > new_cost) {
                dp[cr - 1][cc] = new_cost;
                q.push(make_pair(-new_cost, make_pair(cr - 1, cc)));
            }
        }
        if (cc + 1 < field[cr].size()) {
            int new_cost = curr_cost + field[cr][cc + 1];

            if (dp[cr][cc + 1] > new_cost) {
                dp[cr][cc + 1] = new_cost;
                q.push(make_pair(-new_cost, make_pair(cr, cc + 1)));
            }
        }
        if (cc - 1 >= 0) {
            int new_cost = curr_cost + field[cr][cc - 1];

            if (dp[cr][cc - 1] > new_cost) {
                dp[cr][cc - 1] = new_cost;
                q.push(make_pair(-new_cost, make_pair(cr, cc - 1)));
            }
        }
    }

    cout << dp[field.size() - 1][field[0].size() - 1] << "\n";

    return 0;
}