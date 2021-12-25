#include <bits/stdc++.h>

using namespace std;

const int MAX_S = 10;
const int ADJ_N = 8;

int dx[8] = {0, 0, -1, 1, -1, 1, -1, 1};
int dy[8] = {-1, 1, 0, 0, -1, 1, 1, -1};

vector<vector<int> > readInput() {
    vector<vector<int> > input(MAX_S, vector<int>(MAX_S));

    for (int i = 0; i < MAX_S; i++) {
        string line;
        cin >> line;

        assert(line.size() == MAX_S);

        for (int j = 0; j < line.size(); j++) {
            input[i][j] = (int) line[j] - '0';
        }
    }

    return input;
}

bool inside(int i, int j) {
    return min(i, j) >= 0 && i < MAX_S && j < MAX_S;
}

int runStep(vector<vector<int> >& arg) {
    int flashes = 0;
    vector<vector<bool> > hasFlased(MAX_S, vector<bool>(MAX_S, false));

    // Increase by 1
    for (int i = 0; i < MAX_S; i++) {
        for (int j = 0; j < MAX_S; j++) {
            arg[i][j] += 1;
        }
    }

    while (true) {
        bool hasRun = false;

        for (int i = 0; i < MAX_S && !hasRun; i++) {
            for (int j = 0; j < MAX_S && !hasRun; j++) {
                if (hasFlased[i][j]) {
                    continue;
                }
                if (arg[i][j] <= 9) {
                    continue;
                }

                hasRun = true;
                flashes += 1;
                hasFlased[i][j] = true;

                for (int k = 0; k < ADJ_N; k++) {
                    int ni = i + dx[k];
                    int nj = j + dy[k];

                    if (!inside(ni, nj)) {
                        continue;
                    }

                    arg[ni][nj] += 1;
                }
            }
        }

        if (!hasRun) {
            break;
        }
    }

    for (int i = 0; i < MAX_S; i++) {
        for (int j = 0; j < MAX_S; j++) {
            if (arg[i][j] > 9) {
                arg[i][j] = 0;
            }
        }
    }

    return flashes;
}

void printInput(vector<vector<int> > arg) {
    for (int i = 0; i < MAX_S; i++) {
        for (int j = 0; j < MAX_S; j++) {
           cout << arg[i][j];
        }
        cout << endl;
    }
    cout << endl;
}

int main() {
    vector<vector<int> > input = readInput();
    long long flashSum = 0;
    const int STEPS = 100;

    for (int i = 0; i < STEPS; i++) {
        printInput(input);
        flashSum += runStep(input);
    }

    cout << flashSum << "\n";

    return 0;
}