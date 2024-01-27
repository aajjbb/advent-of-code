import sys
import re

def add_edge(graph, from_node, to_node):
    if from_node not in graph:
        graph[from_node] = [to_node]
    else:
        graph[from_node].append(to_node)

def count_child(graph, node):
    queue = [node]
    visited = [node]

    while queue != []:
        curr_node = queue.pop(0)

        if curr_node not in graph:
            continue

        for next_node in graph[curr_node]:
            if next_node in visited:
                continue
            visited.append(next_node)
            queue.append(next_node)

    return len(visited) - 1

if __name__ == "__main__":
    START_NODE = "shiny gold"

    bag_graph = {}

    for line in sys.stdin:
        line_content = str(line).replace('\r\n', '')

        root_node, child_node = re.search(
            "(\w+\s\w+)\s\w+\s\w+\s\w+\s(\w+\s\w*)", line_content).groups()

        if child_node != 'other bags':
            add_edge(bag_graph, child_node, root_node)

        other_child = line_content.split(',')[1:]

        for unparsed_child in other_child:
            child = re.search("\s\d*\s(\w+\s\w+)", unparsed_child).group(1)
            add_edge(bag_graph, child, root_node)

    print(count_child(bag_graph, START_NODE))
