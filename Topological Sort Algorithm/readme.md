# Topological Sort Algorithm

Topological sort is a graph algorithm used to linearly order the vertices of a directed acyclic graph (DAG). In a DAG, each edge has a direction, and there are no cycles (i.e., paths that start and end at the same vertex). The topological sort arranges the vertices in a way that for every directed edge from vertex `u` to vertex `v`, `u` comes before `v` in the linear order.

## Application

Topological sort has several applications in computer science and real-world scenarios:

1. Task Scheduling: It can be used to schedule tasks in a way that all dependencies are satisfied before executing a task.

2. Build Systems: In build systems, the order of compilation for different components is determined using topological sort to ensure that all dependencies are built before dependent components.

3. Event Processing: It can be used to process events in the correct order based on their dependencies.

## Algorithm

The topological sort algorithm is based on depth-first search (DFS). It explores the graph in a depth-first manner and places vertices in the output list as they are visited and all their dependencies are explored. The ordering is done in reverse order, so the last explored vertex comes first in the final list.

## Implementation Explanation

The provided Python code demonstrates a topological sort implementation using a depth-first search approach. The function `depthFirstSearch` performs the DFS to traverse the graph and keep track of visited nodes. It uses a set `visited` to mark visited nodes to avoid revisiting them. The `topologicalSort` function initializes an empty list `ordering`, which will store the topologically sorted nodes.

1. The `topologicalSort` function starts by initializing an empty set `visited` to track visited nodes.

2. It then iterates through each node in the graph. If the node is not visited, it calls the `depthFirstSearch` function to perform DFS from that node.

3. The `depthFirstSearch` function starts from a current node and marks it as visited. It explores all its connected nodes and recursively calls `depthFirstSearch` on unvisited nodes.

4. The nodes are inserted at the beginning of the `nodes` list in reverse order during the recursive backtracking step, ensuring the correct topological ordering.

5. The `topologicalSort` function returns the list `ordering`, which contains the nodes in topological order.

## Example

```python
graph = {
    "a": ["d"],
    "b": ["d"],
    "c": ["a", "b"],
    "d": ["g", "h"],
    "e": ["a", "d", "f"],
    "f": ["k", "j"],
    "g": ["i"],
    "h": ["i", "j"],
    "i": ["l"],
    "j": ["m", "l"],
    "k": ["j"],
    "l": [],
    "m": [],
}

sorted_order = topologicalSort(graph)
print(sorted_order)  # Output: ['e', 'f', 'k', 'c', 'b', 'a', 'd', 'h', 'j', 'm', 'g', 'i', 'l']
```

The output is a valid topological order for the given directed acyclic graph. The vertices are ordered in such a way that all dependencies are satisfied before a vertex appears in the list.
