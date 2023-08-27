from graph import Graph, Edge


def eagerPrimsAlgo(graph: Graph, start: int = 0):
    n = len(graph.getAdjList())
    m = n - 1  # m is the number of edges in the minimum spanning tree
    priority_q = {}
    priority_q[0] = Edge(-1, 0, -float('inf'))
    visited = set()
    edge_count, mst_cost = 0, 0
    mst_edges = [None for _ in range(m)]

    relaxEdges(graph, start, visited, priority_q)

    while len(priority_q) != 0 and edge_count != m:
        edge = sorted(list(priority_q.values()), key=lambda x: x.weight).pop(
            1
        )
        del priority_q[edge.to]

        if edge.to in visited:
            continue

        mst_edges[edge_count] = [edge.origin, edge.to]
        edge_count += 1

        mst_cost += edge.weight

        relaxEdges(graph, edge.to, visited, priority_q)

    return mst_cost, mst_edges


def relaxEdges(graph: Graph, node: int, visited: set, priority_q: list):
    visited.add(node)

    edges = graph.getAdjList().get(node)
    for edge in edges:
        dest_node = edge.to

        if dest_node in visited:
            continue

        if dest_node not in priority_q.keys() or priority_q[dest_node].weight> edge.weight:
            priority_q[dest_node] = edge


graph = Graph()

graph.addEdge(0, 1, 10)
graph.addEdge(0, 2, 1)
graph.addEdge(0, 3, 4)
graph.addEdge(1, 0, 10)
graph.addEdge(1, 2, 3)
graph.addEdge(1, 4, 1)
graph.addEdge(2, 0, 1)
graph.addEdge(2, 1, 3)
graph.addEdge(2, 3, 2)
graph.addEdge(2, 5, 8)
graph.addEdge(3, 0, 4)
graph.addEdge(3, 2, 2)
graph.addEdge(3, 5, 2)
graph.addEdge(3, 6, 7)
graph.addEdge(4, 1, 1)
graph.addEdge(4, 5, 1)
graph.addEdge(4, 7, 8)
graph.addEdge(5, 2, 8)
graph.addEdge(5, 3, 2)
graph.addEdge(5, 4, 1)
graph.addEdge(5, 6, 6)
graph.addEdge(5, 7, 9)
graph.addEdge(6, 3, 7)
graph.addEdge(6, 5, 6)
graph.addEdge(6, 7, 12)
graph.addEdge(6, 3, 7)
graph.addEdge(7, 4, 8)
graph.addEdge(7, 5, 9)
graph.addEdge(7, 6, 12)


print(eagerPrimsAlgo(graph))
