def eagerPrimsAlgo(graph: dict, start: int = 0):
    n = len(graph)
    m = n - 1  # m is the number of edges in the minimum spanning tree
    priority_q = {}
    priority_q[0] = [None, 0, -float('inf')]
    visited = set()
    edge_count, mst_cost = 0, 0
    mst_edges = [None for _ in range(m)]

    relaxEdges(graph, start, visited, priority_q)

    while len(priority_q) != 0 and edge_count != m:
        [node, dest, cost] = sorted(list(priority_q.values()), key = lambda x: x[2]).pop(1)
        del priority_q[dest]

        if dest in visited:
            continue
        

        mst_edges[edge_count] = [node, dest]
        edge_count+=1

        mst_cost += cost

        relaxEdges(graph, dest, visited, priority_q)

    return mst_cost, mst_edges



def relaxEdges(graph: dict, node: int, visited: set, priority_q: list):
    visited.add(node)

    edges = graph.get(node)
    for edge in edges:
        dest_node = edge[0]

        if dest_node in visited: continue

        if dest_node not in priority_q.keys() or priority_q[dest_node][2] > edge[1]:
            priority_q[dest_node] = [node, *edge]

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

print(eagerPrimsAlgo(graph))