#include <bits/stdc++.h>

using namespace std;

int main() {
    const int MAX_PASS = 1010;

    int low, high;
    char letter;
    char password[MAX_PASS];

    int valid = 0;

    while (scanf("%d-%d %c: %s", &low, &high, &letter, &password) == 4) {
        //cerr << low << " " << high << " " << letter << " " << password << endl;
        bool on_l = password[low - 1] == letter;
        bool on_r = password[high - 1] == letter;

        if (on_l ^ on_r) {
            valid += 1;
        }

    }

    printf("%d\n", valid);

    return 0;
}