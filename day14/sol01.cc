#include <bits/stdc++.h>

using namespace std;

const int RUNS = 10;

void doRun(list<char>& arg, map<string, char> mapper) {
    list<char>::iterator it = arg.begin();

    while (it != arg.end()) {
        list<char>::iterator it_next = next(it);

        if (it_next == arg.end()) {
            break;
        }

        string elem = string(1, *it) + string(1, *it_next);

        if (mapper.find(elem) != mapper.end()) {
            char addition = mapper[elem];
            //cerr << elem << endl;
            it = next(it);
            arg.insert(it, addition);
        } else {
            it = next(it);
        }
    }
}

list<char> toList(string arg) {
    list<char> ans;

    for (int i = 0; i < arg.size(); i++) {
        ans.emplace_back(arg[i]);
    }

    return ans;
}

int calcResult(const list<char> arg) {
    map<char, int> cnt;

    for (const auto elem : arg) {
        cnt[elem] += 1;
    }

    int c_min = INT_MAX;
    int c_max = INT_MIN;

    for (const auto elem : cnt) {
        c_min = min(c_min, elem.second);
        c_max = max(c_max, elem.second);
    }

    return c_max - c_min;
}

int main() {
    string base_input;
    string match_elem, delim, inserted_string;
    
    map<string, char> mapper;

    cin >> base_input;

    while (cin >> match_elem >> delim >> inserted_string) {
        // Inserted_string is always a single char string.
        assert(inserted_string.size() == 1);
        mapper[match_elem] = inserted_string[0];
    }

    list<char> input_list = toList(base_input);

    for (int i = 0; i < RUNS; i++) {
        doRun(input_list, mapper);

        //  for (const auto elem : input_list) {
        //     cerr << elem;
        // }
        // cerr << endl;
    }

    cout << calcResult(input_list) << endl;

    return 0;
}