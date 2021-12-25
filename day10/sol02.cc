#include <bits/stdc++.h>

using namespace std;

string OPEN = "([{<";
string CLOSED = ")]}>";

map<char, int> scoreKeeper = {
    {')', 1},
    {']', 2},
    {'}', 3},
    {'>', 4}
};

bool isOpen(char c) {
    return OPEN.find(c) != string::npos;
}

bool isClosed(char c) {
    return CLOSED.find(c) != string::npos;
}

bool matchChar(char a, char b) {
    int pos_a = OPEN.find(a);
    int pos_b = CLOSED.find(b);

    if (pos_a == string::npos || pos_b == string::npos) {
        return false;
    }

    return pos_a == pos_b;
}

char closedCompanion(char c) {
    return CLOSED[OPEN.find(c)];
}

bool isCorrupted(string arg) {
    stack<char> stk;

    for (int i = 0; i < (int) arg.size(); i++) {
        if (isOpen(arg[i])) {
            stk.push(arg[i]);
        } else {
            // Incomplete case.
            if (stk.empty()) {
                return true;
            }

            if (matchChar(stk.top(), arg[i])) {
                stk.pop();
            } else {
                return true;
            }
        }
    }

    return false;
}

long long calcScore(string arg) {
    long long score = 0;
    stack<char> stk;

    for (int i = 0; i < (int) arg.size(); i++) {
        if (isOpen(arg[i])) {
            stk.push(arg[i]);
        } else {
            // Incomplete case.
            assert(!stk.empty());

            if (matchChar(stk.top(), arg[i])) {
                stk.pop();
            }
        }
    }

    string missing = "";

    while (!stk.empty()) {
        missing += closedCompanion(stk.top());
        stk.pop();
    }

    for (int i = 0; i < (int) missing.size(); i++) {
        score *= 5;
        score += scoreKeeper[missing[i]];
    }

    return score;
}

long long middleScore(vector<long long> arg) {
    int l = 0, h = arg.size() - 1;

    while (l <= h) {
        int m = (l + h) / 2;

        int s = 0;
        int b = 0;

        for (int i = 0; i < arg.size(); i++) {
            if (arg[i] < arg[m]) {
                s += 1;
            }
            if (arg[i] > arg[m]) {
                b += 1;
            }
        }

        if (s == b) {
            return arg[m];
        } else if (s < b) {
            h = m - 1;
        } else {
            l = m + 1;
        }
    }
    return 0;
}

int main() {
    string arg;

    vector<long long> scores;

    while (cin >> arg) {
        if (isCorrupted(arg)) {
            continue;
        }
        //cout << arg << " " << calcScore(arg) << endl;
        scores.push_back(calcScore(arg));
    }

    sort(scores.begin(), scores.end());
    scores.erase(unique(scores.begin(), scores.end()), scores.end());

    cout << scores[scores.size() / 2] << endl;

    return 0;
}