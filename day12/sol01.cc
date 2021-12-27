#include <bits/stdc++.h>

using namespace std;

const int MAXS = 30;
const int MAXN = 1000;

int global_node_counter = 1;
map<string, int> node_mapper;
map<int, string> rev_mapper;

int get_node_id(string arg) {
    if (node_mapper.find(arg) != node_mapper.end()) {
        return node_mapper[arg];
    }

    node_mapper[arg] = global_node_counter;
    rev_mapper[global_node_counter] = arg;

    global_node_counter++;

    return node_mapper[arg];
}

bool is_big(int node) {
    string rev = rev_mapper[node];

    for (int i = 0; i < rev.size(); i++) {
        if (islower(rev[i])) {
            return false;
        }
    }

    return true;
}

int count_paths(int curr_node, int end_node, const vector<vector<int> >& G, set<int> visited) {
    if (curr_node == end_node) {
        return 1;
    }

    visited.insert(curr_node);
    int ans = 0;

    for (int i = 0; i < (int) G[curr_node].size(); i++) {
        int next = G[curr_node][i];
        cerr << curr_node << " " << next << endl;
        if (is_big(next) || !visited.count(next)) {
            set<int> new_visited = visited;
            new_visited.insert(next);
            ans += count_paths(next, end_node, G, visited);
        }
    }

    return ans;
}

vector<string> tokenize(string const &str, const char delim) {
    vector<std::string> out;
    size_t start;
    size_t end = 0;
 
    while ((start = str.find_first_not_of(delim, end)) != string::npos) {
        end = str.find(delim, start);
        out.push_back(str.substr(start, end - start));
    }

    return out;
}

int main() {
    string input;
    vector<vector<int> > G(MAXN, vector<int>());

    while (cin >> input) {
        vector<string> tokens = tokenize(input, '-');
        
        string A = tokens[0];
        string B = tokens[1];

        int id_a = get_node_id(A);
        int id_b = get_node_id(B);

        G[id_a].push_back(id_b);
        G[id_b].push_back(id_a);

       // cerr << A << " " << B << endl;
        //cerr << id_a << " " << id_b << endl;
    }

    int ans = count_paths(get_node_id("start"), get_node_id("end"), G, set<int>());

    cout << ans << endl;

    return 0;
}