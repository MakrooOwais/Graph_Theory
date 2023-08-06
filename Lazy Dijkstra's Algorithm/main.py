def lazyDejkstras(graph: dict, start: int):
    results = {i: float("inf") for i in range(len(graph.keys()))}
    visited = set()
    results[start] = 0

    priority_q = [[start, 0]]

    while len(priority_q) != 0:
        node = min(priority_q, key=lambda n: n[1])
        priority_q.remove(node)
        visited.add(node[0])

        for neighbor in graph.get(node[0]):
            if neighbor[0] in visited:
                continue

            results[neighbor[0]] = min(
                results[node[0]] + neighbor[1], results[neighbor[0]]
            )
            priority_q.append([neighbor[0], results[neighbor[0]]])

    return results


graph = {0: [[1, 4], [2, 1]], 1: [[3, 1]], 2: [[1, 2], [3, 5]], 3: [[4, 3]], 4: []}

if __name__ == "__main__":
    results = lazyDejkstras(graph, 0)
    print(results)
