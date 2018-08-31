import sys

from Read_Graph import read_graph


def find_negative_cycles(name_txt_file):
    with open(name_txt_file) as f:
        graph = read_graph(f)
    node_list = list(graph.keys())

    source = node_list[0]
    distance = {node: float("inf") for node in node_list}
    distance[source] = 0

    for i in range(len(node_list) - 1):
        for node_u in node_list:
            if distance[node_u] != float("inf"):
                for node_v, weight in graph[node_u].items():
                    if distance[node_u] + weight < distance[node_v]:
                        distance[node_v] = distance[node_u] + weight

    for node_u in node_list:
        if distance[node_u] != float("inf"):
            for node_v, weight in graph[node_u].items():
                if distance[node_u] + weight < distance[node_v]:
                    print ("Graph contains a negative cycle")
                    return

    print ("Graph has no negative cycle")
    return


if __name__ == "__main__":
    find_negative_cycles(sys.argv[1])
