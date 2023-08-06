def eagerDejkstras(graph: dict, start: int):
    results = {i: float("inf") for i in graph.keys()}
    results[start] = 0

    visited = set()
    prev = {i: None for i in graph.keys()}

    priority_q = {start: 0}

    while len(priority_q) != 0:
        node = min(priority_q.items(), key=lambda n: n[1])
        priority_q.pop(node[0])
        visited.add(node[0])

        for neighbor in graph.get(node[0]):
            if neighbor[0] in visited:
                continue
            if results[neighbor[0]] < results[node[0]] + neighbor[1]:
                continue
            results[neighbor[0]] = results[node[0]] + neighbor[1]
            prev[neighbor[0]] = node[0]
            priority_q[neighbor[0]] = results[neighbor[0]]

    return results, prev


def findShortestPath(graph: dict, start: int, end: int):
    n_steps, prev = eagerDejkstras(graph, start)
    path = []
    if n_steps[end] == float("inf"):
        return path

    current_node = end

    while current_node != start:
        path.insert(0, current_node)
        current_node = prev[current_node]

    path.insert(0, start)

    return path


graph_1 = {0: [[1, 4], [2, 1]], 1: [[3, 1]], 2: [[1, 2], [3, 5]], 3: [[4, 3]], 4: []}
graph_2 = {
    0: [[1, 5], [2, 1]],
    1: [[2, 2], [3, 3], [4, 20]],
    2: [[1, 3], [4, 12]],
    3: [[2, 3], [4, 2], [5, 6]],
    4: [[5, 1]],
    5: [],
}

if __name__ == "__main__":
    results = eagerDejkstras(graph_1, 0)
    path = findShortestPath(graph_1, 0, 4)
    print(results)
    print(path)
    results = eagerDejkstras(graph_2, 0)
    path = findShortestPath(graph_2, 0, 5)
    print(results)
    print(path)
