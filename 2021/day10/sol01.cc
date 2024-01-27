#include <bits/stdc++.h>

using namespace std;

string OPEN = "([{<";
string CLOSED = ")]}>";

map<char, int> scoreKeeper = {
    {')', 3},
    {']', 57},
    {'}', 1197},
    {'>', 25137}
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

int calcScore(string arg) {
    stack<char> stk;

    for (int i = 0; i < (int) arg.size(); i++) {
        if (isOpen(arg[i])) {
            stk.push(arg[i]);
        } else {
            // Incomplete case.
            if (stk.empty()) {
                return 0;
            }

            if (matchChar(stk.top(), arg[i])) {
                stk.pop();
            } else {
                return scoreKeeper[arg[i]];
            }
        }
    }

    return 0;
}

int main() {
    string arg;
    long long sum = 0;

    while (cin >> arg) {
        //cout << arg << " " << calcScore(arg) << endl;
        sum += calcScore(arg);
    }

    cout << sum << endl;

    return 0;
}