#include <bits/stdc++.h>

using namespace std;

const int MAX_LINES = 5;

vector<string> tokenize(string &str, string delim) {
    vector<string> out;

	size_t start;
	size_t end = 0;

	while ((start = str.find_first_not_of(delim, end)) != string::npos) {
		end = str.find(delim, start);
		out.push_back(str.substr(start, end - start));
	}

    return out;
}

vector<int> convert_vec(vector<string> input) {
    vector<int> out;

    for (int i = 0; i < input.size(); i++) {
        out.push_back(stoi(input[i]));
    }

    return out;
}

int main() {
    // Input Reading.
    string input_buffer;
    cin >> input_buffer;

    vector<int> drawn_numbers = convert_vec(tokenize(input_buffer, ","));
    vector<vector<vector<int> > > boards;

    while (true) {
        vector<vector<int> > board(MAX_LINES, vector<int>(MAX_LINES));
        bool valid = true;

        for (int i = 0; valid && i < MAX_LINES; i++) {
            for (int j = 0; valid && j < MAX_LINES; j++) {
                if (!(cin >> board[i][j])) {
                    valid = false;
                    break;
                } else {
                    //cout << board[i][j] << " ";
                }
            }
            //cout << endl;
        }
        if (!valid) {
            break;
        }
        boards.push_back(board);
    }

    // Bingo game.
    map<int, int> num_visited;
    vector<bool> completed_board(boards.size(), false);

    for (auto& drawn_number : drawn_numbers) {
        num_visited[drawn_number] = 1;

        for (int b = 0; b < boards.size(); b++) {
            bool completed = false;
            int unmarked_sum = 0;

            vector<int> row_c(MAX_LINES);
            vector<int> col_c(MAX_LINES);

            for (int i = 0; i < MAX_LINES; i++) {
                for (int j = 0; j < MAX_LINES; j++) {
                    if (num_visited.count(boards[b][i][j])) {
                        row_c[i] += 1;
                        col_c[j] += 1;
                    } else {
                        unmarked_sum += boards[b][i][j];
                    }
                }
            }

            for (int i = 0; i < MAX_LINES; i++) {
                if (row_c[i] == MAX_LINES || col_c[i] == MAX_LINES) {
                    completed = true;
                }
            }

            if (completed && !completed_board[b]) {
                cout << unmarked_sum * drawn_number << "\n";
                completed_board[b] = true;
            }
        }
    }

    return 0;
}