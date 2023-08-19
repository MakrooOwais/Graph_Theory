def findEularianPath(graph: dict):
    n = len(graph)
    m = numEdges(graph)

    n_in = [0 for _ in range(n)]
    n_out = [0 for _ in range(n)]

    path = []

    countInOutDegrees(graph, n_in, n_out)

    if not graphHasEularianPath(graph, n_in, n_out):
        return None

    start = findStartNode(graph, n_in, n_out)

    dfs(graph, start, n_out, path)

    path.insert(0, start)

    if len(path) == m + 1:
        return path

    return None


def numEdges(graph: dict) -> int:
    num = 0
    for node in graph.keys():
        num += len(graph[node])

    return num


def countInOutDegrees(graph: dict, n_in: list[int], n_out: list[int]):
    for node in graph.keys():
        for edge in graph.get(node):
            n_out[int(node)] += 1
            n_in[int(edge)] += 1


def graphHasEularianPath(graph: dict, n_in: list[int], n_out: list[int]) -> bool:
    n = len(graph)
    start_nodes = 0
    end_nodes = 0

    for i in range(n):
        if abs(n_out[i] - n_in[i]) > 1:
            return False

        elif n_out[i] - n_in[i] == 1:
            start_nodes += 1

        elif n_in[i] - n_out[i] == 1:
            end_nodes += 1

    return (end_nodes == 0 and start_nodes == 0) or (
        end_nodes == 1 and start_nodes == 1
    )


def findStartNode(graph: dict, n_in: list[int], n_out: list[int]):
    n = len(graph)
    start = 0

    for i in range(n):
        if n_out[i] - n_in[i] == 1:
            return i

        if n_out[i] > 0:
            start = i

    return start


def dfs(graph: dict, at: int, n_out: list[int], path: list):
    while n_out[at] != 0:
        n_out[at] -= 1
        next_edge = graph.get(str(at))[n_out[at]]

        dfs(graph, int(next_edge), n_out, path)

        path.insert(0, int(next_edge))


graph = {
    "0": [],
    "1": ["2", "3"],
    "2": ["2", "4", "4"],
    "3": ["1", "2", "5"],
    "4": ["3", "6"],
    "5": ["6"],
    "6": ["3"],
}




print(' -> '.join([str(i) for i in findEularianPath(graph)]))
