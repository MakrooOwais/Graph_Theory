# Articulation Point Detection in Graphs

This Python script implements an algorithm for detecting articulation points in an undirected graph. An articulation point, also known as a cut vertex, is a node within the graph whose removal increases the number of connected components. The algorithm efficiently identifies these critical nodes and returns a list of them.

## What are Articulation Points?

In graph theory, articulation points play a crucial role in understanding a graph's structure and connectivity. Removing an articulation point can lead to the creation of multiple disconnected subgraphs, highlighting its importance in maintaining graph connectivity.

## How the Algorithm Works

The algorithm employs a depth-first search (DFS) traversal to detect articulation points. It utilizes two key arrays: `low_link` and `ids`, as well as a `is_art` array to mark nodes as articulation points.

- `ids` array stores the order in which nodes are visited during the DFS traversal.
- `low_link` array stores the minimum order (id) reachable from a node through the edges of its subtree.
- `is_art` array indicates whether a node is an articulation point.

## Depth-First Search (DFS) Traversal

The algorithm performs a DFS traversal of the graph starting from each unvisited node. During the traversal, it assigns an id to each node in the `ids` array and updates the `low_link` values.

1. For each node, it initializes its `id` and `low_link` to the current value of a counter.
2. As the DFS explores neighbors of a node, it recursively updates `low_link` values based on the lowest id reachable from that subtree.
3. If `low_link` of a neighbor is greater than or equal to the `id` of the current node, then the current node is an articulation point.

## Resultant Articulation Points

By comparing the `low_link` values and the `id` of nodes, the algorithm efficiently identifies articulation points. When it detects a node as an articulation point, it marks the corresponding index in the `is_art` array as `True`.

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
art_points = findArtPoints(graph)
print(art_points)
```

The output will be a list of articulation points:

```python
[2, 3, 5]
```

This indicates that nodes 2, 3, and 5 are articulation points in the given graph.

In summary, the articulation point detection algorithm efficiently explores the graph's structure using DFS and identifies nodes where their removal would increase the number of connected components. This algorithm is valuable for understanding the critical nodes in a graph that significantly affect its connectivity and structure.
