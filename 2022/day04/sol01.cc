#include <bits/stdc++.h>

using namespace std;

bool isFullyEnclosed(pair<int, int> a, pair<int, int> b) {
    if (b.first >= a.first && b.second <= a.second) {
        return true;
    } else {
        return false;
    }
}

int main() {
    string input;
    int count = 0;

    while (cin >> input) {
        pair<int, int> pa, pb;
        sscanf(input.c_str(), "%d-%d,%d-%d", &pa.first, &pa.second, &pb.first, &pb.second);
        if (isFullyEnclosed(pa, pb) || isFullyEnclosed(pb, pa)) {
            count += 1;
        }
    }

    cout << count << "\n";
    return 0;
}