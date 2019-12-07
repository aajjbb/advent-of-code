import sys

def add_edge(graph, node_a, node_b):
    if node_a not in graph:
        graph[node_a] = []

    if node_b not in graph:
        graph[node_b] = []

    graph[node_a].append(node_b)
    graph[node_b].append(node_a)
    return graph

def dijkstra(graph, start_node):
    q = [start_node]
    dist = {start_node: 0}

    # Using simple queue instead of priority, since
    # there's plenty of time.
    while q:
        curr_node = q.pop()

        if not curr_node in graph:
            continue

        for node in graph[curr_node]:
            if node in dist and dist[node] <= dist[curr_node] + 1:
                continue
            dist[node] = dist[curr_node] + 1
            q.append(node)

    return dist

if __name__ == "__main__":
    START_NODE = "YOU"
    FINAL_NODE = "SAN"
    graph = {}

    for line in sys.stdin:
        tokens = line.strip().split(")")
        a = tokens[0]
        b = tokens[1]

        graph = add_edge(graph, a, b)

    DISTANCES = dijkstra(graph, START_NODE)

    print(DISTANCES[FINAL_NODE] - 2)
