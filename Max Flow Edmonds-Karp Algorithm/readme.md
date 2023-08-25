# Edmonds-Karp Algorithm for Maximum Flow - Explanation and Implementation

The provided code implements the **Edmonds-Karp algorithm**, which is used to solve the maximum flow problem in a network flow graph. Let's understand what the algorithm is, the differences between the DFS and BFS approaches, and how the implementation works.

## Maximum Flow Problem

The maximum flow problem deals with finding the maximum flow that can be sent from a designated source node to a designated sink node in a flow network. In the context of transportation, this could represent the maximum amount of goods that can be transported from a source to a destination through various paths.

## Edmonds-Karp Algorithm

The Edmonds-Karp algorithm is a specific implementation of the Ford-Fulkerson method for solving the maximum flow problem. It uses **Breadth-First Search (BFS)** for finding augmenting paths from the source to the sink. The algorithm is guaranteed to terminate because each augmenting path increases the flow value by at least one unit, and the algorithm stops when no augmenting path is found.

## Key Differences between DFS and BFS Approaches

1. **DFS (Depth-First Search) Approach**: The DFS approach explores paths in a depth-first manner. It doesn't necessarily find the shortest augmenting path, which can lead to inefficiencies and longer runtime in some cases.

2. **BFS (Breadth-First Search) Approach**: The BFS approach explores paths in a breadth-first manner. It always finds the shortest augmenting path in terms of the number of edges, ensuring that the algorithm terminates in a reasonable amount of time.

## Implementation Explanation

The provided code contains two classes: `Edge` and `Graph`, along with the Edmonds-Karp algorithm implementation.

- `Edge` class: Represents an edge in the flow network. It has attributes to track the origin and destination nodes, flow capacity, residual capacity, current flow, and whether it's a residual edge.

- `Graph` class: Represents the flow network. It has methods to add edges and get the edges. It also maintains a dictionary of edges for each node.

- `bfs(graph: Graph, visited: list, visited_token: int)`: This function performs a BFS search to find an augmenting path from the source to the sink.

- `edmondKarp(graph: Graph)`: The main algorithm. It repeatedly calls `bfs` to find augmenting paths, calculates the bottleneck capacity of the path, augments the flow, and repeats until no more augmenting paths can be found.

## Example Usage

1. The provided example creates a flow network using the `Graph` class and adds edges. Then, the `edmondKarp` function is called on this network to find the maximum flow.

## Conclusion

The Edmonds-Karp algorithm is a powerful method for solving the maximum flow problem in a flow network. Its use of BFS ensures efficiency and termination, making it a practical choice for real-world applications like network flow optimization, transportation planning, and resource allocation. The provided implementation showcases the algorithm's core logic and demonstrates how it can be applied to solve maximum flow problems.
