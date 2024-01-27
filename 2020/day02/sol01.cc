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
        int len = strlen(password);
        int letter_cnt = 0;

        for (int i = 0; i < len; i++) {
            if (password[i] == letter) {
                letter_cnt += 1;
            }
        }

        if (letter_cnt >= low && letter_cnt <= high) {
            valid += 1;
        }
    }

    printf("%d\n", valid);

    return 0;
}