#include <bits/stdc++.h>

using namespace std;

const int SIGNAL_PATTERN = 10;
const int OUTPUT_VALUE = 4;

int main() {
    vector<vector<string> > input_patterns, output_values;

    // Input Reading.
    while (true) {
        string dummy_separator;

        vector<string> input_pattern(SIGNAL_PATTERN);
        vector<string> output_value(OUTPUT_VALUE);
        bool valid_read = true;

        for (int i = 0; i < SIGNAL_PATTERN; i++) {
            if (!(cin >> input_pattern[i])) {
                valid_read = false;
            }
        }

        cin >> dummy_separator;

        for (int i = 0; i < OUTPUT_VALUE; i++) {
            if (!(cin >> output_value[i])) {
                valid_read = false;
            }
        }

        if (!valid_read) {
            break;
        }

        input_patterns.push_back(input_pattern);
        output_values.push_back(output_value);
    }

    int ans = 0;

    for (int i = 0; i < output_values.size(); i++) {
        for (int j = 0; j < OUTPUT_VALUE; j++) {
            int size = output_values[i][j].size();

            if (size == 2 || size == 3 || size == 4 || size == 7) {
                ans += 1;
            }
        }
    }

    cout << ans << "\n";

    return 0;
}