#include <bits/stdc++.h>

using namespace std;

const int MAXN = 110;

long long dp[MAXN][MAXN];

long long calculate(int pos, int last_used, const vector<int>& adapters) {
    if (pos == adapters.size()) {
        return last_used == adapters.back();
    } else if (adapters[pos] - last_used > 3) {
        return 0;
    } else {
        long long& ans = dp[pos][last_used];

        if (ans == -1) {
            ans = calculate(pos + 1, last_used, adapters);

            if (adapters[pos] - last_used <= 3) {
                ans += calculate(pos + 1, adapters[pos], adapters);
            }
        }

        return ans;
    }
}

int main() {
    vector<int> adapters;
    int tmp;

    while (cin >> tmp) {
        adapters.emplace_back(tmp);
    }

    sort(adapters.begin(), adapters.end());

    adapters.emplace_back(adapters.back() + 3);

    memset(dp, -1, sizeof(dp));

    cout << calculate(0, 0, adapters) << "\n";

    return 0;
}