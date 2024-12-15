#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> va, vb;
    int buff_a, buff_b;

    while (cin >> buff_a >> buff_b) {
        va.emplace_back(buff_a);
        vb.emplace_back(buff_b);
    }

    sort(va.begin(), va.end());
    sort(vb.begin(), vb.end());

    assert(va.size() == vb.size());

    long long diff_sum = 0;

    for (int i = 0; i < (int) va.size(); i++) {
        diff_sum += abs(va[i] - vb[i]);
    }

    cout << diff_sum << "\n";
    return 0;
}