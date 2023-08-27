from graph import Graph


def breadth_first_search(graph: Graph, start: str):
    queue = []
    queue.append(start)

    while len(queue) > 0:
        node = queue.pop(0)
        print(node)
        for edge in graph.getAdjList().get(node):
            queue.append(edge.to)


graph = Graph()

graph.addEdge("a", "b")
graph.addEdge("a", "c")
graph.addEdge("b", "d")
graph.addEdge("c", "e")
graph.addEdge("d", "f")

breadth_first_search(graph, "a")
print(graph.getAdjList())
print(graph.getAdjMat())
