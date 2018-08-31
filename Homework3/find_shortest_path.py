import sys

from Read_Graph import read_graph


def find_shortest_path(name_txt_file, source, destination):
    with open(name_txt_file) as f:
        graph = read_graph(f)

    source = float(source)
    destination = float(destination)
    shortest_path_node = set()
    shortest_path_node.add(source)
    shortest_path = dict()
    shortest_path[source] = [(source, 0.), ]

    from heapq import heappush, heappop

    min_dist_heap = []
    for node, weight in graph[source].items():
        heappush(min_dist_heap, (weight, source, node))

    while min_dist_heap:
        weight_uv, node_u, node_v = heappop(min_dist_heap)
        if node_v not in shortest_path_node:
            shortest_path_node.add(node_v)
            shortest_path[node_v] = [pair for pair in shortest_path[node_u]]
            shortest_path[node_v].append((node_v, weight_uv))
            for node, weight in graph[node_v].items():
                heappush(min_dist_heap, (weight, node_v, node))

    if destination in shortest_path:
        return (sum([value[1] for value in shortest_path[destination]]),
                [value[0] for value in shortest_path[destination]])


if __name__ == "__main__":
    print(find_shortest_path(sys.argv[1], sys.argv[2], sys.argv[3]))
