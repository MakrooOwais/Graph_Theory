from collections import deque
from graph import Graph


def depth_first_search(graph: Graph, start: str):
    stack = deque()
    stack.append(start)

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for edge in graph.getAdjList().get(current):
            stack.append(edge.to)


graph = Graph()

graph.addEdge("a", "b")
graph.addEdge("a", "c")
graph.addEdge("b", "d")
graph.addEdge("c", "e")
graph.addEdge("d", "f")

depth_first_search(graph, "a")
