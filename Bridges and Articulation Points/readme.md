# Bridge Detection in Graphs

This Python script implements an algorithm for detecting bridges in an undirected graph. A bridge is an edge within the graph, such that removing it would increase the number of connected components in the graph. The algorithm effectively identifies these bridges and returns a list of them.

## How the Algorithm Works

The bridge detection algorithm employs a depth-first search (DFS) approach to traverse through the graph and identify bridges. It maintains two important arrays: `low_link` and `ids`.

- `ids` array stores the order in which nodes are visited during the DFS traversal.
- `low_link` array stores the minimum order (id) reachable from a node through the edges of its subtree.

The algorithm starts by visiting each node in the graph. During the traversal, it identifies and records the bridges that it encounters.

## Depth-First Search (DFS) Traversal

The algorithm performs a DFS traversal of the graph starting from each unvisited node. During the traversal, it assigns an id to each node in the `ids` array and updates the `low_link` values.

1. For each node, it initializes its `id` and `low_link` to the current value of a counter.
2. As the DFS explores neighbors of a node, it recursively updates `low_link` values based on the lowest id reachable from that subtree.
3. If the `low_link` value of a neighbor is greater than the `id` of the current node, then the edge connecting them is a bridge.

## Resultant Bridges

The algorithm's DFS traversal efficiently identifies bridges by comparing the `low_link` values and the `id` of nodes. When it detects an edge (u, v) as a bridge, it adds [u, v] to the list of bridges.

## Example

Consider the following input graph represented as an adjacency list:

```python
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
```

Upon running the algorithm:

```python
bridges = findBridges(graph)
print(bridges)
```

The output will be a list of bridges:

```python
[[3, 4], [2, 3], [2, 5]]
```

This indicates that the edges (2, 3) and (2, 5) are bridges in the given graph.

In summary, the bridge detection algorithm efficiently explores the graph's structure using DFS and identifies bridges by comparing node `ids` and `low_link` values. This makes it a valuable tool for understanding the connectivity of a graph and analyzing its vulnerabilities.
