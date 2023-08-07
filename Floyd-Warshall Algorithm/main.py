def detectNegativeCycles(memo, next_node, n):
    # This function is used to detect negative cycles in the given graph using Floyd-Warshall algorithm.
    # It takes the memo table, the "next_node" table, and the number of nodes in the graph as inputs.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If there is a shorter path from node i to node j through node k, then there is a negative cycle.
                # In this case, we mark memo[i][j] as -infinity and next_node[i][j] as -1.
                # This information will be later used to reconstruct the negative cycle path.
                if memo[i][j] > memo[i][k] + memo[k][j]:
                    memo[i][j] = -float("inf")
                    next_node[i][j] = -1

    return memo, next_node


def reconstructPath(memo, next_node, start, end, node_num):
    # This function is used to reconstruct the path between two nodes (start and end) in the graph.
    path = []

    # If there is no path from start to end (i.e., memo[start][end] is infinity), return an empty path.
    if memo[start][end] == float("inf"):
        return path

    at = start

    # Traverse the "next_node" table to reconstruct the path from start to end.
    while at != end:
        path.append(node_num[at])
        at = next_node[at][end]
        if at == -1:
            return None  # If there is a negative cycle, return None to indicate that no valid path exists.

    if next_node[at][end] == -1:
        return None  # If there is a negative cycle, return None to indicate that no valid path exists.
    path.append(node_num[end])  # Add the destination node to the path.

    return path


def floydWarshall(graph: list):
    # This function implements the Floyd-Warshall algorithm to find the shortest paths between all pairs of nodes in the graph.
    n = len(graph)
    memo = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            memo[i][j] = graph[i][j]

    next_node = [[None for i in range(n)] for j in range(n)]

    # Initialize the "next_node" table with next_node node information for each edge in the graph.
    for i in range(n):
        for j in range(n):
            if memo[i][j] != float("inf"):
                next_node[i][j] = j

    # Floyd-Warshall algorithm's main loop to find the shortest paths.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if memo[i][j] > memo[i][k] + memo[k][j]:
                    memo[i][j] = memo[i][k] + memo[k][j]
                    next_node[i][j] = next_node[i][k]

    # After finding the shortest paths, detect and mark negative cycles using the detectNegativeCycles function.
    # memo, next_node = detectNegativeCycles(memo, next_node, n)

    return memo, next_node


graph = [
    [0, 4, 1, float("inf")],
    [float("inf"), 0, 6, float("inf")],
    [4, 1, 0, 2],
    [float("inf"), float("inf"), float("inf"), 0],
]

node_num = {0: "A", 1: "B", 2: "C", 3: "D"}

floydWarshall(graph)
print(reconstructPath(*floydWarshall(graph), 0, 1, node_num))
