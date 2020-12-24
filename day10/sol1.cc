#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> adapters;
    int diff[4] = {};
    int tmp;

    adapters.emplace_back(0);

    while (cin >> tmp) {
        adapters.emplace_back(tmp);
    }

    sort(adapters.begin(), adapters.end());

    adapters.emplace_back(adapters.back() + 3);

    for (int i = 1; i < adapters.size(); i++) {
        diff[adapters[i] - adapters[i - 1]] += 1;
    }

    cout << diff[1] << " " << diff[3] << endl;
    cout << diff[1] * diff[3] << "\n";

    return 0;
}