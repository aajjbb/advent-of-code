import sys
import re


def add_edge(graph, from_node, to_node, count):
    if from_node not in graph:
        graph[from_node] = [(to_node, int(count))]
    else:
        graph[from_node].append((to_node, int(count)))


def count_child(graph, node, count):
    if not node in graph:
        return 0

    bag_count = 0

    for next_node, next_count in graph[node]:
        child_result = count_child(graph, next_node, next_count)

        bag_count += next_count * (child_result + 1)

    return bag_count


if __name__ == "__main__":
    START_NODE = "shiny gold"

    bag_graph = {}

    for line in sys.stdin:
        line_content = str(line).replace('\r\n', '')

        root_node, child_count, child_node = re.search(
            "(\w+\s\w+)\s\w+\s\w+\s(\w+)\s(\w+\s\w*)", line_content).groups()

        if child_node != 'other bags':
            add_edge(bag_graph, root_node, child_node, child_count)

        other_child = line_content.split(',')[1:]

        for unparsed_child in other_child:
            child_count, child = re.search("\s(\d*)\s(\w+\s\w+)",
                                           unparsed_child).groups()
            add_edge(bag_graph, root_node, child, child_count)

    print(count_child(bag_graph, START_NODE, 0))
