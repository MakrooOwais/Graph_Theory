def findSSCs(graph: dict):
    n = len(graph)

    visited = set()
    low_link = [float("inf") for _ in range(n)]

    for i in graph.keys():
        sscs = dfs(graph, i, low_link, visited)

    return sscs


def dfs(
    graph: dict,
    node: int,
    low_link: list,
    visited: set,
    stack: list = [],
    sscs: list = [],
):
    visited.add(node)
    stack.append(node)
    low_link[node] = node

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, low_link, visited, stack, sscs)
        
        if neighbor in stack:
            print(neighbor)
            low_link[node] = min(low_link[neighbor], low_link[node])

    if node == low_link[node]:
        if len(stack) > 1:
            ssc = []
            while True:
                stack_node = stack.pop()
                ssc.insert(0, stack_node)
                low_link[stack_node] = node
                if stack_node == node:
                    if len(ssc) > 1:
                        sscs.append(ssc)
                    break
            

    return sscs


graph = {0: [1], 1: [2], 2: [0], 3: [4, 7], 4: [5], 5: [0, 6], 6: [0, 2, 4], 7: [3, 5]}


print(findSSCs(graph))
