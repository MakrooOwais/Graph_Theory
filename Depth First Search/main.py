from collections import deque


def depth_first_search(graph: dict, start: str):
    stack = deque()
    stack.append(start)

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph.get(current):
            stack.append(neighbor)


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

depth_first_search(graph, "a")
