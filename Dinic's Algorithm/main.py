from graph import Graph


def dinicMaxFlow(graph: Graph, start: int, sink: int) -> int:
    n = len(graph.getAdjMat())
    level = [-1] * n
    maxFlow = 0

    while bfs(graph, start, sink, level):
        next_node = [0] * n
        
        
        flow = dfs(graph, start, sink, next_node, level, float("inf"))

        while flow != 0:
            maxFlow += flow
            flow = dfs(graph, start, sink, next_node, level, float("inf"))

    return maxFlow


def bfs(graph: Graph, start: int, sink: int, level: list) -> bool:
    queue = []
    queue.append(start)
    for i in range(len(level)):
        level[i] = -1
    level[start] = 0

    while len(queue) != 0:
        node = queue.pop(0)

        for edge in graph.getAdjList().get(node):
            cap = edge.getRemainingCapacity()

            if cap > 0 and level[edge.to] == -1:
                level[edge.to] = level[node] + 1
                queue.append(edge.to)

    return level[sink] != -1


def dfs(
    graph: Graph, node: int, sink: int, next_node: list[int], level: list[int], flow: int
):
    if node == sink:
        return flow

    n = len(graph.getAdjList().get(node))

    while next_node[node] < n:
        edge = graph.getAdjList().get(node)[next_node[node]]
        cap = edge.getRemainingCapacity()
        
        if cap > 0 and level[edge.to] == level[node] + 1:
            bottleneck = dfs(graph, edge.to, sink, next_node, level, min(flow, cap))

            if bottleneck > 0:
                edge.augment(bottleneck)
                return bottleneck

        next_node[node] += 1

    return 0


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


print(dinicMaxFlow(graph, 0, 10))
