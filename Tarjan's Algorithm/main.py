def findSSCs(graph: dict):
    n = len(graph)

    visited = set()
    low_link = [float("inf") for _ in range(n)]

    sccs = []

    for i in graph.keys():
        sccs = dfs(graph, i, low_link, visited)

    
    return sccs


def dfs(
    graph: dict,
    node: int,
    low_link: list,
    visited: set,
    stack: list = [],
    sccs: list = [],
):
    visited.add(node)
    stack.append(node)
    low_link[node] = node

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, low_link, visited, stack, sccs)

        if neighbor in stack:
            low_link[node] = min(low_link[neighbor], low_link[node])

    if node == low_link[node]:
        if len(stack) > 1:
            scc = []
            while True:
                stack_node = stack.pop()
                scc.insert(0, stack_node)
                low_link[stack_node] = node
                if stack_node == node:
                    if len(scc) > 1:
                        sccs.append(scc)
                    break
        
    return sccs


graph_1 = {
    0: [1],
    1: [2],
    2: [0],
    3: [4, 7],
    4: [5],
    5: [0, 6],
    6: [0, 2, 4],
    7: [3, 5],
}
graph_2 = {0: [1], 1: [2, 3], 2: [3, 5], 3: [0, 4], 4: [5], 5: [6], 6: [4]}



# print(findSSCs(graph_1))
# print('--------')
print(findSSCs(graph_2))
