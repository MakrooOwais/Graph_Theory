def lazyPrimsAlgo(graph: dict, start: int = 0):
    n = len(graph)
    priority_q = []
    visited = set()
    m = n - 1  # m is the number of edges in the minimum spanning tree
    edge_count, mst_cost = 0, 0
    mst_edges = [None for _ in range(m)]

    addEdges(graph, priority_q, int(start), visited)

    while len(priority_q) != 0 and edge_count != m:
        print(priority_q)
        priority_q = sorted(priority_q, key=lambda x: x[2])
        [node, dest, cost] = priority_q.pop(0)

        if dest in visited:
            continue

        mst_edges[edge_count] = [node, dest]
        edge_count += 1

        mst_cost += cost

        addEdges(graph, priority_q, dest, visited)

    if edge_count != m:
        return None, None

    return mst_cost, mst_edges


def addEdges(graph: dict, priority_q: list, node: int, visited: set):
    visited.add(node)

    edges = graph.get(node)

    for edge in edges:
        if edge[0] not in visited:
            priority_q.append([node, *edge])

    return node


graph = {
    0: [[1, 10], [2, 1], [3, 4]],
    1: [[0, 10], [2, 3], [4, 0]],
    2: [[0, 1], [1, 3], [3, 2], [5, 8]],
    3: [[0, 4], [2, 2], [5, 2], [6, 7]],
    4: [[1, 0], [5, 1], [7, 8]],
    5: [[2, 8], [3, 2], [4, 1], [6, 6], [7, 9]],
    6: [[3, 7], [5, 6], [7, 12]],
    7: [[4, 8], [5, 9], [6, 12]],
}


print(lazyPrimsAlgo(graph))
