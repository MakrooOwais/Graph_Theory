def findArtPoints(graph: dict):
    n = len(graph)

    ids = [0 for _ in range(n)]
    low_link = [0 for _ in range(n)]
    is_art = [False for _ in range(n)]
    visited = set()

    for node in graph.keys():
        if node not in visited:
            out_edges = dfs(graph, node, node, -1, visited, low_link, ids, is_art)
            is_art[node] = out_edges > 1

    art_points = [i for i in range(n) if is_art[i]]

    return art_points


def dfs(
    graph: dict,
    root: int,
    current_node: int,
    parent: int,
    visited: set,
    low_link: list,
    ids: list,
    is_art: list,
    id=0,
    out_edges: int = 0,
):
    if parent == root: 
        out_edges += 1
    visited.add(current_node)
    id = id + 1
    low_link[current_node] = ids[current_node] = id

    for neighbor in graph[current_node]:
        if neighbor == parent: continue
        if neighbor not in visited:
            dfs(graph, root, neighbor, current_node, visited, low_link, ids, is_art, id, out_edges)
            low_link[current_node] = min(low_link[current_node], low_link[neighbor])
            # The less than case is for articulation points found using bridges and the equal case is for articulation points found using cycles
            if ids[current_node] <= low_link[neighbor]:
                is_art[current_node] = True

        else:
            low_link[current_node] = min(low_link[current_node], ids[neighbor])
    
    return out_edges


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

print(findArtPoints(graph))
