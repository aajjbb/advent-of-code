#include <bits/stdc++.h>

using namespace std;

const int BOARD_LEN = 10;
const int MAX_PTS = 1000;
const int DICE_RUNS = 3;
const int PLAYER_NUM = 2;

int dice_curr_value = 1;

int dice_value() {
    int ans = dice_curr_value;

    dice_curr_value += 1;

    if (dice_curr_value > 100) {
        dice_curr_value = 1;
    }

    return ans;
}

int main() {
    // -1 on the initial positions.
    // We're working with [0..BOARD_LEN-1] instead of
    // [1..BOARD_LEN]
    vector<int> player_pos = {3, 8};
    vector<int> player_pts = {0, 0};

    int rolls = 0;
    int curr_p = 0;

    while (*max_element(player_pts.begin(), player_pts.end()) < MAX_PTS) {
        int sum = 0;

        for (int i = 0; i < DICE_RUNS; i++) {
            sum += dice_value();
            rolls += 1;
        }

        player_pos[curr_p] = ((player_pos[curr_p] + sum) % BOARD_LEN);
        player_pts[curr_p] += player_pos[curr_p] + 1;

        //cout << "pos = " << player_pos[curr_p] << endl;
        //cout << "pts = " << player_pts[0] << " " << player_pts[1] << endl;

        curr_p += 1;
        curr_p %= PLAYER_NUM;
    }

    cout << rolls * (*min_element(player_pts.begin(), player_pts.end())) << "\n";

    return 0;
}