# Trajan's Algorithm for Strongly Connected Components (SSCs) Detection

This Python script implements Trajan's algorithm, a powerful approach for detecting Strongly Connected Components (SSCs) in a directed graph. Trajan's algorithm efficiently identifies maximal subgraphs where there is a directed path between every pair of nodes.

## What are Strongly Connected Components (SSCs)?

In a directed graph, a strongly connected component is a subset of nodes where every node is reachable from every other node within the subset. Detecting SSCs is essential for understanding the connectivity and structure of directed graphs.

## Trajan's Algorithm Overview

Trajan's algorithm, based on depth-first search (DFS), is a linear-time algorithm that identifies SCCs. It utilizes two crucial arrays: `ids` and `low_link`.

- `ids` array assigns unique IDs to each node during the traversal.
- `low_link` array stores the lowest ID reachable from the current node through its subtree.

## Depth-First Search (DFS) with Trajan's Algorithm

1. For each unvisited node, Trajan's algorithm performs a DFS traversal.
2. During traversal, it assigns incremental IDs to nodes and updates the `low_link` values.
3. As the traversal progresses, if a node's `low_link` matches its own ID, it marks the root of a new SCC.
4. It efficiently identifies SCCs by backtracking through the stack while updating the `low_link` values.

## Example and Explanation

Consider the following input graph represented as an adjacency list:

```python
graph = {
    0: [1],
    1: [2],
    2: [0],
    3: [4, 7],
    4: [5],
    5: [0, 6],
    6: [0, 2, 4],
    7: [3, 5]
}
```

Running the algorithm:

```python
sccs = findSSCs(graph)
print(sccs)
```

Output:

```python
[[0, 2, 1], [4, 6, 5], [7, 3]]
```

Explanation of Trajan's Algorithm in the Code:
1. The algorithm initializes variables and arrays.
2. It iterates through nodes and initiates DFS for unvisited nodes.
3. During the DFS traversal, the `ids` and `low_link` arrays are updated.
4. When a node's `low_link` equals its own ID, it is marked as the root of an SCC.
5. The algorithm backtracks through the stack to identify SCCs.
6. SCCs are appended to the result list.

Trajan's algorithm efficiently identifies SCCs by utilizing the concept of `ids` and `low_link` arrays. It performs a linear-time DFS traversal and backtracking to find SCCs in directed graphs.

In summary, Trajan's algorithm is a powerful method for detecting SSCs, providing insights into the connectivity and organization of directed graphs. This algorithm is particularly valuable for analyzing large and complex networks.
