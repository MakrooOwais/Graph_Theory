def findBridges(graph: dict):
    n = len(graph)

    ids = [0 for _ in range(n)]
    low_link = [0 for _ in range(n)]
    visited = set()

    for node in graph.keys():
        if node not in visited:
            bridges = dfs(graph, node, -1, visited, low_link, ids)

    return bridges


def dfs(graph: dict, node: int, parent_node: int, visited: set, low_link: list, ids: list, id: int=0, bridges: list=[]):
    visited.add(node)
    id = id + 1
    low_link[node] = ids[node] = id

    for neighbor in graph[node]:
        if neighbor == parent_node:
            continue
        if neighbor not in visited:
            dfs(graph, neighbor, node, visited, low_link, ids, id, bridges)
            low_link[node] = min(low_link[node], low_link[neighbor])
            if ids[node] < low_link[neighbor]:
                bridges.append([node, neighbor])
        else:
            low_link[node] = min(low_link[node], ids[neighbor])

    return bridges


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 8],
    6: [5, 7],
    7: [6, 8],
    8: [5, 7],
}

print(findBridges(graph))
