from collections import deque


def breadth_first_search(graph: dict, start: str):
    queue = deque()
    queue.append(start)

    while len(queue) > 0:
        current = queue.popleft()
        print(current)
        for neighbor in graph.get(current):
            queue.append(neighbor)


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

breadth_first_search(graph, "a")
