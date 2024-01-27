#include <bits/stdc++.h>

using namespace std;

int main() {
    string buffer;
    vector<string> road;

    int trees = 0;

    while (cin >> buffer) {
        road.emplace_back(buffer);
    }

    int i = 0;
    int j = 0;

    while (i < road.size()) {
        if (road[i][j] == '#') {
            trees += 1;
        }
        j = (j + 3) % road[i].size();
        i += 1;
    }

    cout << trees << endl;
    return 0;
}