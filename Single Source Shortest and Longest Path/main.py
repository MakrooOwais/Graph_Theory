graph = {
    "a": [["b", 3], ["c", 6]],
    "b": [["c", 4], ["d", 4], ["e", 11]],
    "c": [["d", 8], ["g", 11]],
    "d": [["e", -4], ["f", 5], ["g", 2]],
    "e": [["h", 9]],
    "f": [["h", 1]],
    "g": [["h", 2]],
    "h": [],
}

def sssp(graph: dict, source:str):
    results = {key : float('inf') for key in graph.keys()}
    results[source] = 0

    for node in graph.keys():
        for neighbor in graph.get(node):
            results[neighbor[0]] = min(results[neighbor[0]], results[node] + neighbor[1])

    return results

def sslp(graph: dict, source:str):
    results = {key : float('-inf') for key in graph.keys()}
    results[source] = 0

    for node in graph.keys():
        for neighbor in graph.get(node):
            results[neighbor[0]] = max(results[neighbor[0]], results[node] + neighbor[1])

    return results

print(sslp(graph, 'a'))
print(sssp(graph, 'a'))
