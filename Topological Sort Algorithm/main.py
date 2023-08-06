def depthFirstSearch(graph: dict, current_node: str, visited: set, nodes: list = []):
    visited.add(current_node)

    connected_nodes = graph.get(current_node)

    for dest_node in connected_nodes:
        if dest_node not in visited:
            nodes, visited = depthFirstSearch(graph, dest_node, visited, nodes)

    nodes.insert(0, current_node)

    return nodes, visited


def topologicalSort(graph: dict):
    visited = set()

    ordering = []

    for node in graph.keys():
        if node not in visited:
            ordering, visited = depthFirstSearch(graph, node, visited, ordering)

    return ordering


graph = {
    "a": ["d"],
    "b": ["d"],
    "c": ["a", "b"],
    "d": ["g", "h"],
    "e": ["a", "d", "f"],
    "f": ["k", "j"],
    "g": ["i"],
    "h": ["i", "j"],
    "i": ["l"],
    "j": ["m", "l"],
    "k": ["j"],
    "l": [],
    "m": [],
}


top = topologicalSort(graph)
print(top)
