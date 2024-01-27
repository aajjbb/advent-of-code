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

int count_paths(int curr_node, int end_node, const vector<vector<int> >& G, map<int, int> visited, bool has_visited_small_twice {
   if (curr_node == end_node) {
        return 1;
    }

    visited[curr_node] += 1;
    int ans = 0;

    for (int i = 0; i < (int) G[curr_node].size(); i++) {
        int next = G[curr_node][i];
        //cerr << curr_node << " " << next << endl;

        if (is_big(next) || (visited[next] == 0) || (visited[next] == 1 && !has_visited_small_twice && rev_mapper[next] != "start")) {
            map<int, int> new_visited = visited;
            //new_visited[next] += 1;

            bool new_visited_twice = new_visited[next] > 0  && !is_big(next) ? true : has_visited_small_twice;

            ans += count_paths(next, end_node, G, visited, new_visited_twice);
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

        //cerr << A << " " << B << endl;
        //cerr << id_a << " " << id_b << endl;
    }

    int ans = count_paths(get_node_id("start"), get_node_id("end"), G, map<int, int>(), false);

    cout << ans << endl;

    return 0;
}