# Eager Prim's Algorithm - Explanation and Implementation

The provided code implements **Eager Prim's algorithm**, an alternative approach to finding the Minimum Spanning Tree (MST) of a weighted graph. Eager Prim's algorithm is based on maintaining a priority queue (heap) of potential edges and adding the lowest-weight edge that connects the already included vertices to an outside vertex. Let's explore the concept of the algorithm, the implementation, and the example usage.

## Prim's Algorithm Concept

Eager Prim's algorithm is another way to find the MST of a weighted graph. Like the Lazy Prim's algorithm, it grows the MST from an initial vertex, but instead of using a lazy approach, it maintains a priority queue to eagerly add edges with the lowest weight.

## Implementation Explanation

The provided code contains the following components:

-   **Graph Class (`graph`)**: An instance of the custom `Graph` class that contains edges and their weights.

-   **`eagerPrimsAlgo` Function**: The main algorithm function. It initializes a priority queue (`priority_q`) to keep track of potential edges. It starts with an empty MST and adds edges eagerly while ensuring that no cycle is formed.

-   **`relaxEdges` Function**: A helper function that updates the priority queue based on the new vertex added to the MST. It compares the weight of the potential edge and updates the queue if the current edge has a lower weight.

## Key Steps of the Algorithm

1. **Initialization**: Initialize the priority queue with the start vertex (`0` by default) having a dummy edge with negative infinity weight.

2. **Main Loop**: Iterate while the priority queue is not empty and the number of added edges is less than `n - 1` (where `n` is the number of vertices).

3. **Eager Edge Selection**: Select the lowest-weight edge from the priority queue. This edge connects a vertex from the MST to a vertex outside the MST.

4. **Priority Queue Update**: Remove the selected edge from the priority queue.

5. **MST Update**: Add the selected edge to the MST and update the MST's total cost.

6. **Neighbor Exploration**: Update the priority queue with edges connected to the newly added vertex.

7. **Termination**: The algorithm terminates when the priority queue is empty or when the MST has `n - 1` edges.

## Example Usage

The provided example creates a weighted graph using the `Graph` class and adds edges with their weights. Then, the `eagerPrimsAlgo` function is called on this graph to find the minimum cost of the MST and the edges included in it.

## Advantages of Eager Prim's Algorithm

-   **Eager Approach**: Eager Prim's algorithm eagerly selects edges based on their weights, potentially reducing the number of edge selections compared to the lazy approach.

-   **Efficiency**: Eager Prim's algorithm efficiently selects edges using a priority queue, resulting in a time complexity similar to that of Lazy Prim's algorithm (O(E log V)).

## Conclusion

Eager Prim's algorithm offers another approach to finding the minimum spanning tree in a weighted graph. The provided implementation demonstrates the algorithm's core logic and how it can be applied to find the MST's minimum cost and included edges. By maintaining a priority queue and eagerly selecting edges with the lowest weights, this algorithm can efficiently construct the MST.
