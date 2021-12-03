#include <bits/stdc++.h>

using namespace std;

const int MAX_BITS = 31;

int main(void) {
    string input;
    vector<string> S;

    while (cin >> input) {
        reverse(input.begin(), input.end());

        S.push_back(input);
    }

    map<int, int> cnt[MAX_BITS];

    for (int i = 0; i < MAX_BITS; i++) {
        for (int j = 0; j < S.size(); j++) {
            if (i >= S[j].size()) {
                break;
            }
            int digit = S[j][i] - '0';

            cnt[i][digit] += 1;
        }
    }

    long long a = 0;
    long long b = 0;

    for (int i = 0; i < MAX_BITS; i++) {
        //cout << cnt[i][0] << " " << cnt[i][1] << endl;
        if (cnt[i][0] > cnt[i][1]) {
            a |= (1 << i);
        }
        if (cnt[i][0] < cnt[i][1]) {
            b |= (1 << i);
        }
    }

    cout << a * b << "\n";

    return 0;
}