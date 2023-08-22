# Ford-Fulkerson Algorithm - Explanation and Implementation

The **Ford-Fulkerson algorithm** is a method for computing the maximum flow in a flow network, which is a directed graph with capacities assigned to its edges. The goal is to find the maximum amount of flow that can be sent from a source vertex to a sink vertex while respecting the capacity constraints of the edges. The algorithm repeatedly augments paths from the source to the sink with additional flow until no more augmenting paths can be found. This implementation uses classes and objects to represent the graph and edges, making the code more organized and readable.

## Key Concepts

Before diving into the implementation, let's understand the key concepts involved:

1. **Flow Network**: A directed graph where each edge has a capacity, representing the maximum flow it can carry.
2. **Source and Sink**: The source vertex is where the flow originates, and the sink vertex is the destination.
3. **Augmenting Paths**: Paths from the source to the sink where each edge has available capacity for additional flow.
4. **Residual Graph**: A graph that reflects the available capacity on edges and the flow through them.

## Implementation Explanation

### Edge Class

The `Edge` class represents an edge in the graph. It includes the following attributes and methods:

-`origin`, `to`: Vertices that the edge connects.
-`residual`: Reference to the residual edge in the opposite direction.
-`flow_capacity`: Maximum flow the edge can carry.
-`flow`: Current flow through the edge.
-`is_residual`: Indicates if the edge is a residual edge.

### Graph Class

The `Graph` class represents the flow network and includes these methods:

-`addEdge`: Adds an edge to the graph with its corresponding residual edge.
-`getEdges`: Returns the edges of the graph.

### Depth-First Search (DFS)

The `dfs` function performs a depth-first search to find augmenting paths in the graph. It takes the following parameters:

-`graph`: The flow network graph.
-`node`: The current node being explored.
-`flow`: The current flow value.
-`visited`: A list indicating whether a node has been visited during this search.
-`visited_token`: A unique identifier for marking visited nodes.

The `dfs` function searches for augmenting paths from the source to the sink. It updates the `visited` list and calculates the bottleneck capacity along the path.

### Ford-Fulkerson Algorithm

The `fordFulkerson` function implements the Ford-Fulkerson algorithm. It iteratively finds augmenting paths and updates the flow through the edges. The algorithm works as follows:

1. Initialize variables: `visited_token`, `max_flow`.
2. Use DFS to find an augmenting path from the source to the sink.
3. While an augmenting path is found:
    - Add the flow through the path to the `max_flow`.
    - Use DFS to find the next augmenting path.
4. Return `max_flow`.

## Example

Consider the following flow network:

```text
Source -> 0 -> 1 -> 4 -> Sink
        |    |    |
        v    v    v
        2    5    6
        |    |    |
        v    v    v
        3    8    5
        |    |    |
        v    v    v
        6    9    7
          \       /
           -------
```

Applying the Ford-Fulkerson algorithm on this network, we find the maximum flow from the source to the sink.

## Conclusion

The Ford-Fulkerson algorithm is a fundamental algorithm in network flow optimization. It uses augmenting paths to determine the maximum amount of flow that can be sent from a source to a sink in a flow network. The implementation provided here represents the graph using classes and objects, making it more modular and understandable. The algorithm ensures that the flow across the network respects the capacity constraints of the edges, providing a practical solution for various real-world problems.
