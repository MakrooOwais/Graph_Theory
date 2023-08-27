from graph import Graph

import math

SOURCE = 0
SINK = 10

def dfs(graph: Graph, node: int, flow: int, visited: list, visited_token: int, delta: int):
    if node == SINK: return flow

    visited[node] = visited_token

    for edge in graph.getAdjList().get(node):
        cap = edge.getRemainingCapacity()

        if cap >= delta and visited[edge.to] != visited_token:
            bottleneck = dfs(graph, edge.to, min(flow, cap), visited, visited_token, delta)

            if bottleneck > 0:
                edge.augment(bottleneck)
                return bottleneck
    
    return 0



def capacityScaling(graph: Graph):
    delta = graph.max_edge_cap
    delta = int(math.log(delta, 2))

    visited_token = 1
    max_flow = 0

    visited = [0] * (len(graph.getAdjList()))

    while delta > 0:
        flow = dfs(graph, SOURCE, float('inf'), visited, visited_token, delta)
        visited_token += 1
        while flow != 0:
            max_flow += flow
            flow = dfs(graph, SOURCE, float('inf'), visited, visited_token, delta)
            visited_token += 1
        delta /= 2

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


print(capacityScaling(graph))
