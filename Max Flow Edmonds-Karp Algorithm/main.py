from graph import Graph

SOURCE = 0
SINK = 10


def bfs(graph: Graph, visited: list, visited_token: int):
    queue = []
    visited[SOURCE] = visited_token
    queue.append(SOURCE)

    path = [None] * len(graph.getEdges())

    while len(queue) != 0:
        next_node = queue.pop(0)

        if next_node == SINK:
            break

        for edge in graph.getEdges().get(next_node):
            cap = edge.getRemainingCapacity()

            if cap > 0 and visited[edge.to] != visited_token:
                visited[edge.to] = visited_token
                path[edge.to] = edge
                queue.append(edge.to)

    if path[SINK] == None:
        return 0

    bottleneck = float("inf")

    edge = path[SINK]

    while edge != None:
        bottleneck = min(bottleneck, edge.getRemainingCapacity())
        edge = path[edge.origin]

    edge = path[SINK]

    while edge != None:
        edge.augment(bottleneck)
        edge = path[edge.origin]

    return bottleneck


def edmondKarp(graph: Graph):
    visited_token = 1
    max_flow = 0

    visited = [0] * (len(graph.getEdges()))
    flow = bfs(graph, visited, visited_token)
    visited_token += 1

    while flow != 0:
        max_flow += flow
        flow = bfs(graph, visited, visited_token)
        visited_token += 1

    return max_flow


graph = Graph()

graph.addEdge(0, 1, 10)
graph.addEdge(0, 2, 5)
graph.addEdge(0, 3, 10)
graph.addEdge(1, 4, 10)
graph.addEdge(2, 3, 10)
graph.addEdge(3, 6, 15)
graph.addEdge(4, 2, 20)
graph.addEdge(4, 7, 13)
graph.addEdge(5, 4, 3)
graph.addEdge(5, 2, 15)
graph.addEdge(6, 5, 4)
graph.addEdge(6, 9, 10)
graph.addEdge(7, 8, 10)
graph.addEdge(7, 10, 15)
graph.addEdge(8, 5, 10)
graph.addEdge(8, 6, 7)
graph.addEdge(9, 10, 10)


print(edmondKarp(graph))
