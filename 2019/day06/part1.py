import sys

def add_edge(graph, node_a, node_b):
    if node_a not in graph:
        graph[node_a] = []

    graph[node_a].append(node_b)

    return graph

def bfs(graph, start_node):
    q = [start_node]
    dist = {start_node: 0}

    while q:
        curr_node = q.pop()

        if not curr_node in graph:
            continue

        for node in graph[curr_node]:
            dist[node] = dist[curr_node] + 1
            q.append(node)

    return dist

if __name__ == "__main__":
    START_NODE = "COM"
    graph = {}

    for line in sys.stdin:
        tokens = line.strip().split(")")
        a = tokens[0]
        b = tokens[1]

        graph = add_edge(graph, a, b)

    DISTANCES = bfs(graph, START_NODE)

    print(sum(DISTANCES.values()))
