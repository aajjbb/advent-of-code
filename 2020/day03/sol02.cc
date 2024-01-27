#include <bits/stdc++.h>

using namespace std;

int count_trees(const vector<string> road, const int add_i, const int add_j) {
    int trees = 0;

    int i = 0;
    int j = 0;

    while (i < road.size()) {
        if (road[i][j] == '#') {
            trees += 1;
        }
        j = (j + add_j) % road[i].size();
        i += add_i;
    }

    return trees;
}

int main() {
    string buffer;
    vector<string> road;

    long long trees = 1;

    while (cin >> buffer) {
        road.emplace_back(buffer);
    }

    trees *= count_trees(road, 1, 1);
    trees *= count_trees(road, 1, 3);
    trees *= count_trees(road, 1, 5);
    trees *= count_trees(road, 1, 7);
    trees *= count_trees(road, 2, 1);

    cout << trees << endl;

    return 0;
}