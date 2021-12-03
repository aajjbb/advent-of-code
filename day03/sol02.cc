#include <bits/stdc++.h>

using namespace std;

const int MAX_BITS = 30;

int to_decimal(const string& input) {
    int ans = 0;

    for (int i = 0; i < input.size(); i++) {
        if (input[i] == '1') {
            ans |= (1 << (input.size() - i - 1));
        }
    }

    return ans;
}

// Return the dominant bit, based on the oxygen/co2 logic.
int get_dominant_bit(const int dominant_kind, const int b0, const int b1) {
    // oxygen
    if (dominant_kind == 0) {
        if (b0 <= b1) {
            return 1;
        } else {
            return 0;
        }
    } else {
        if (b1 >= b0) {
            return 0;
        } else {
            return 1;
        }
    }
}

int filter_values(vector<string> input, const int dominant_kind) {
    for (int bit = 0; bit < MAX_BITS; bit++) {
        if (input.size() == 1) {
            break;
        }

        int b0 = 0;
        int b1 = 0;

        for (int i = 0; i < input.size(); i++) {
            if (bit >= input.size()) {
                break;
            }

            int digit = input[i][bit] - '0';

            if (digit == 0) {
                b0 += 1;
            } else {
                b1 += 1;
            }
        }

        int dominant_bit = get_dominant_bit(dominant_kind, b0, b1);
        vector<string> new_input;

        for (int i = 0; i < input.size(); i++) {
            int digit = input[i][bit] - '0';

            if (digit == dominant_bit) {
                new_input.push_back(input[i]);
            }
        }

        input = new_input;
    }

    return to_decimal(input[0]);
}

int main(void) {
    string input;
    vector<string> S;

    while (cin >> input) {
        S.push_back(input);
    }

    int a = filter_values(S, 0);
    int b = filter_values(S, 1);

    cout << a * b << "\n";

    return 0;
}