import sys
from collections import defaultdict
from copy import copy


def reader():
    graph = defaultdict(dict)
    start = None
    end = None
    edge_num = None
    node_num = None

    for line in sys.stdin:
        if edge_num is None:
            node_num, edge_num = map(int, line.strip().split())

        elif edge_num:
            from_node, to_node, weight = line.strip().split()
            graph[from_node][to_node] = weight
            edge_num -= 1

        else:
            start, end = line.strip().split()

    return start, end, node_num, graph


def main():
    start, end, node_num, graph = reader()
    distances = [9999] * int(node_num)
    distances[int(start) - 1] = 0
    unknown_nodes = graph.copy()

    while unknown_nodes:
        nearest_node = min(unknown_nodes, key=lambda x: distances[int(x) - 1])
        for node, weight in unknown_nodes[nearest_node].items():
            if distances[int(node) - 1] > distances[int(nearest_node) - 1] + \
                    int(weight):
                distances[int(node) - 1] = distances[int(nearest_node) - 1] + \
                                           int(weight)

        del unknown_nodes[nearest_node]  # Удаляем посещенную вершину

    answer = distances[int(end) - 1]  # Расстояние до требуемой вершины
    return answer if answer != 9999 else -1


if __name__ == '__main__':
    print(main())
