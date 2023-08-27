# Lazy Prim's Algorithm - Explanation and Implementation

The provided code implements **Lazy Prim's algorithm** for finding the Minimum Spanning Tree (MST) of a weighted graph. The algorithm works by greedily adding edges of least weight while ensuring that no cycle is formed. Let's dive into the concept of Prim's algorithm, the implementation, and the example usage.

## Prim's Algorithm Concept

Prim's algorithm grows the MST from an initial vertex by repeatedly adding the cheapest edge that connects the growing tree to an outside vertex. It maintains a set of vertices that are included in the MST and a set of vertices that are not yet included. In each step, it adds the lowest-weight edge that connects a vertex from the included set to a vertex from the excluded set.

## Implementation Explanation

The provided code contains the following components:

-   **Graph Class (`graph`)**: An instance of the custom `Graph` class that contains edges and their weights.

-   **`lazyPrimsAlgo` Function**: The main algorithm function. It initializes a priority queue (`priority_q`) to keep track of edges with their weights. It starts with an empty MST and adds edges greedily while ensuring that no cycle is formed.

-   **`addEdges` Function**: A helper function that adds edges connected to a given node to the priority queue.

## Key Steps of the Algorithm

1. **Initialization**: Initialize the priority queue with edges connected to the start vertex (`0` by default).

2. **Main Loop**: Iterate while the priority queue is not empty and the number of added edges is less than `n - 1` (where `n` is the number of vertices).

3. **Greedy Edge Selection**: Select the lowest-weight edge from the priority queue. If its destination vertex is already in the MST, skip it to avoid forming a cycle.

4. **MST Update**: Add the selected edge to the MST and update the MST's total cost.

5. **Neighbor Exploration**: Add edges connected to the newly added vertex to the priority queue.

6. **Termination**: The algorithm terminates when the priority queue is empty or when the MST has `n - 1` edges.

## Example Usage

The provided example creates a weighted graph using the `Graph` class and adds edges with their weights. Then, the `lazyPrimsAlgo` function is called on this graph to find the minimum cost of the MST and the edges included in it.

## Advantages of Lazy Prim's Algorithm

-   **Greedy Approach**: Prim's algorithm follows a greedy approach, adding the lowest-weight edges first, which leads to the formation of an MST.

-   **Efficiency**: Lazy Prim's algorithm efficiently selects edges using a priority queue, resulting in a time complexity of O(E log V), where E is the number of edges and V is the number of vertices.

## Conclusion

Lazy Prim's algorithm is a powerful tool for finding the minimum spanning tree in a weighted graph. The provided implementation demonstrates the algorithm's core logic and how it can be applied to find the MST's minimum cost and included edges. This approach efficiently constructs the MST by greedily selecting edges based on their weights and ensuring that cycles are not formed.
