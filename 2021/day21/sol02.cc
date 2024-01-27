#include <bits/stdc++.h>

using namespace std;

const int MAX_PTS = 305;
const int MAX_POS = 15;

const int BOARD_LEN = 10;
const int MAX_SCORE = 21;
const int DICE_RUNS = 3;

pair<long long, long long> dp[MAX_POS][MAX_POS][MAX_PTS][MAX_PTS][3];
int                      memo[MAX_POS][MAX_POS][MAX_PTS][MAX_PTS][3];

pair<long long, long long> rec(int p1_pos, int p2_pos, int p1_pts, int p2_pts, int curr_p) {
    //cout << p1_pts << " " << p2_pts << " " << p1_pos << " "  << p2_pos << endl;
    if (p1_pts >= MAX_SCORE) {
        return make_pair(1, 0);
    }
    if (p2_pts >= MAX_SCORE) {
        return make_pair(0, 1);
    }

    pair<long long, long long>& ans = dp[p1_pos][p2_pos][p1_pts][p2_pts][curr_p];
    int& seen = memo[p1_pos][p2_pos][p1_pts][p2_pts][curr_p];

    if (seen == -1) {
        seen = 1;
        ans = make_pair(0, 0);

        for (int i = 1; i <= DICE_RUNS; i++) {
            for (int j = 1; j <= DICE_RUNS; j++) {
                for (int k = 1; k <= DICE_RUNS; k++) {
                    int new_p1_pos = p1_pos;
                    int new_p2_pos = p2_pos;
                    int new_p1_pts = p1_pts;
                    int new_p2_pts = p2_pts;

                    if (curr_p == 0) {
                        new_p1_pos += i + j + k;
                        new_p1_pos %= BOARD_LEN;
                        new_p1_pts += new_p1_pos + 1;
                    } else {
                        new_p2_pos += i + j + k;
                        new_p2_pos %= BOARD_LEN;
                        new_p2_pts += new_p2_pos + 1;
                    }

                    pair<long long, long long> recurse = rec(new_p1_pos, new_p2_pos, new_p1_pts, new_p2_pts, 1 - curr_p);

                    ans.first  += recurse.first;
                    ans.second += recurse.second;
                }
            }
        }
    }

    return ans;
}

int main() {
    // -1 on the initial positions.
    // We're working with [0..BOARD_LEN-1] instead of
    // [1..BOARD_LEN]

    memset(memo, -1, sizeof(memo));

    pair<long long, long long> ans = rec(3, 8, 0, 0, 0);

    cout << ans.first << " " << ans.second << "\n";
    cout << max(ans.first, ans.second) << "\n";

    return 0;
}