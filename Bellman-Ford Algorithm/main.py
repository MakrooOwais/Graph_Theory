def bellmanFord(graph: dict, start: str):
    result = {}

    for i in graph.keys():
        result[i] = float("inf")

    result[start] = 0

    for node in graph.keys():
        for neighbor in graph[node]:
            result[neighbor[0]] = min(result[node] + neighbor[1], result[neighbor[0]])

    for _ in range(len(graph.keys()) - 1):
        for node in graph.keys():
            for neighbor in graph[node]:
                if result[node] + neighbor[1] < result[neighbor[0]]:
                    result[neighbor[0]] = float("-inf")

    return result


graph = {
    "0": [["1", 5]],
    "1": [["2", 20], ["5", 30], ["6", 60]],
    "2": [["3", 10], ["4", 75]],
    "3": [["2", -15]],
    "4": [["9", 100]],
    "5": [["4", 25], ["6", 5], ["8", 50]],
    "6": [["7", -50]],
    "7": [["8", -10]],
    "8": [],
    "9": [],
}


print(bellmanFord(graph, "0"))
