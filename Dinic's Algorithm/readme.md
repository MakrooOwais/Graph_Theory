# Dinic's Algorithm for Maximum Flow - Explanation and Implementation

**Dinic's Algorithm** is a powerful algorithm used to solve the **Maximum Flow problem** in a network flow graph. This algorithm efficiently finds the maximum flow that can be sent from a source node to a sink node through the network while obeying capacity constraints on the edges.

## Algorithm Overview

Dinic's Algorithm employs two main techniques: **Layering** and **Blocking Flow Paths**. It iteratively builds the **level graph** through **Breadth-First Search (BFS)**, which assigns layers (distances) to the nodes from the source. Then, it uses **Depth-First Search (DFS)** to find augmenting paths along which flow can be increased.

## Implementation Explanation

### Components:

-   **Graph Class (`graph`)**: An instance of the custom `Graph` class that represents the graph's adjacency list and adjacency matrix.

-   **`dinicMaxFlow` Function**: The main function implementing Dinic's Algorithm. It takes the graph, source, and sink as inputs and returns the maximum flow.

-   **`bfs` Function**: Performs a BFS to construct the level graph and assigns layer levels to the nodes.

-   **`dfs` Function**: Recursively searches for augmenting paths using DFS and returns the bottleneck capacity of the path.

## Key Steps of the Algorithm

1. **Layering (BFS)**:

    - Build a level graph by performing a BFS from the source.
    - Assign layer levels to nodes based on their distance from the source.

2. **Blocking Flow Paths (DFS)**:

    - Use DFS to find augmenting paths in the level graph.
    - Keep track of the next unvisited edge index in each node (`next_node` array).
    - Explore paths while maintaining the level constraints and edge capacities.
    - Calculate and return the bottleneck capacity of the path.

3. **Iteration**:
    - Iterate over BFS and DFS steps until no more augmenting paths can be found in the residual graph.

## Example Usage

The provided example creates a graph using the `Graph` class and adds edges between vertices. Then, the `dinicMaxFlow` function is called with the source vertex `0` and the sink vertex `10`. The algorithm calculates and returns the maximum flow from the source to the sink.

## Benefits of Dinic's Algorithm

-   **Efficiency**: Dinic's Algorithm is one of the most efficient algorithms for finding the maximum flow in a network flow graph.

-   **Layering**: The use of layering (BFS) enhances performance by reducing the number of augmenting paths to be considered.

-   **Adaptability**: It can be applied to both unit-capacity and non-unit-capacity graphs.

## Conclusion

Dinic's Algorithm is a sophisticated method for solving the Maximum Flow problem in network flow graphs. By combining BFS-based layering and DFS-based augmenting paths, it efficiently calculates the maximum flow from the source to the sink while respecting edge capacities. The provided implementation exemplifies how Dinic's Algorithm can be applied to solve a network flow problem.
