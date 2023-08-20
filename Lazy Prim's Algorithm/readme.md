# Minimum Spanning Trees (MST) - Problem Statement and Algorithm

In graph theory, a **Minimum Spanning Tree (MST)** of a connected, undirected graph is a subgraph that includes all the vertices of the original graph while minimizing the total sum of edge weights. MSTs have applications in various fields, including network design, clustering, and more. One common algorithm to find an MST is **Prim's Algorithm**. The provided Python code implements Prim's Algorithm to find an MST using a lazy approach.

## Problem Statement

Given an undirected graph, the goal of the MST problem is to find a subgraph that connects all vertices while minimizing the sum of edge weights.

### Input

- **Graph Representation**: The graph is represented as a dictionary, where each vertex is a key, and its value is a list of tuples containing neighboring vertex and edge weight.

### Output

- **Minimum Spanning Tree (MST)**: A list of edges forming the MST and the total cost of the MST.

## Prim's Algorithm

Prim's Algorithm is a greedy algorithm that starts from an arbitrary vertex and iteratively adds the minimum-weight edge that connects a vertex in the MST to a vertex outside the MST. The lazy version of Prim's Algorithm uses a priority queue to keep track of edges with minimum weights that cross the boundary between the MST and the unvisited vertices.

### Algorithm Steps

1. Initialize the priority queue and other necessary variables.
2. Add the starting vertex to the priority queue.
3. While the priority queue is not empty and the number of added edges is less than `n - 1` (where `n` is the number of vertices):
   - Extract the edge with the minimum weight from the priority queue.
   - If the edge connects a vertex that is already in the MST to a vertex outside the MST, skip it.
   - Otherwise, add the edge to the MST, increment the edge count, and update the MST's total cost.
   - Add the neighboring vertices of the new vertex to the priority queue.

### Implementation Details

The provided Python code implements the lazy Prim's Algorithm using the following functions:

- `lazyPrimsAlgo(graph: dict, start: int = 0)`: Finds the MST using lazy Prim's Algorithm.
- `addEdges(graph: dict, priority_q: list, node: int, visited: set)`: Adds edges to the priority queue during the algorithm's execution.

## Example

Consider the following graph:

```python
{
    0: [[1, 10], [2, 1], [3, 4]],
    1: [[0, 10], [2, 3], [4, 0]],
    2: [[0, 1], [1, 3], [3, 2], [5, 8]],
    3: [[0, 4], [2, 2], [5, 2], [6, 7]],
    4: [[1, 0], [5, 1], [7, 8]],
    5: [[2, 8], [3, 2], [4, 1], [6, 6], [7, 9]],
    6: [[3, 7], [5, 6], [7, 12]],
    7: [[4, 8], [5, 9], [6, 12]],
}
```

The minimum spanning tree for this graph can be found using the `lazyPrimsAlgo` function, resulting in a list of edges forming the MST and the total cost of the MST.

```bash
    (20, [[0, 2], [2, 3], [3, 5], [5, 4], [4, 1], [5, 6], [4, 7]])
```

## Conclusion

The Minimum Spanning Tree problem and Prim's Algorithm play a crucial role in optimizing network designs, such as connecting cities with minimal road construction costs or minimizing data transmission costs in communication networks. The lazy approach optimizes the algorithm's efficiency by delaying the consideration of certain edges. The provided code serves as a practical implementation of this algorithm in Python.
