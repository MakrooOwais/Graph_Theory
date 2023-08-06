# Lazy Dijkstra's Algorithm

Dijkstra's algorithm is a famous algorithm used to find the shortest path between a starting node and all other nodes in a weighted graph. The algorithm works by iteratively selecting the node with the smallest distance from the starting node and updating the distances of its neighboring nodes. Lazy Dijkstra's algorithm is a variation of the classic Dijkstra's algorithm that uses a priority queue to efficiently select the node with the minimum distance.

## Lazy Dijkstra's Algorithm Explanation

1. Initialize a dictionary `results` with all nodes having a distance of infinity, except for the starting node, which has a distance of 0.

2. Create an empty set `visited` to keep track of the nodes that have been visited.

3. Set the distance of the starting node to 0 in the `results` dictionary.

4. Initialize a priority queue `priority_q` with the starting node and its distance as the first element.

5. While the priority queue is not empty, repeat the following steps:

   a. Select the node with the minimum distance from the priority queue using the `min` function with a custom lambda function.

   b. Remove the selected node from the priority queue.

   c. Add the selected node to the `visited` set.

6. Iterate through the neighbors of the selected node:

   a. If the neighbor is already visited, continue to the next neighbor.

   b. Calculate the new distance from the starting node to the neighbor by adding the distance from the current node to the neighbor's weight.

   c. Update the distance of the neighbor in the `results` dictionary with the minimum of the current distance and the newly calculated distance.

   d. Add the neighbor and its updated distance to the priority queue.

7. Finally, return the `results` dictionary containing the shortest distance from the starting node to all other nodes.

## Implementation Explanation

The provided Python implementation demonstrates the lazy Dijkstra's algorithm. Here's how it works:

1. The `lazyDejkstras` function takes the graph (in the form of an adjacency list) and the starting node as input and returns a dictionary containing the shortest distance from the starting node to all other nodes.

2. The algorithm uses a priority queue to efficiently select the node with the minimum distance. The priority queue is represented as a list of nodes, where each node is a list containing the node number and its corresponding distance from the starting node.

3. The algorithm starts by initializing the `results` dictionary with all nodes having a distance of infinity, except for the starting node, which has a distance of 0.

4. It then creates an empty set `visited` to keep track of the nodes that have been visited.

5. The starting node is added to the priority queue with a distance of 0.

6. The main loop runs while the priority queue is not empty. In each iteration, the algorithm selects the node with the minimum distance from the priority queue using the `min` function.

7. The selected node is removed from the priority queue and added to the `visited` set.

8. The algorithm iterates through the neighbors of the selected node and updates their distances in the `results` dictionary if a shorter path is found.

9. If a neighbor is already visited, it is skipped to avoid unnecessary calculations.

10. The algorithm continues to explore the graph until all reachable nodes are visited.

11. Finally, the `results` dictionary containing the shortest distances from the starting node to all other nodes is returned.

## Example Output

For the provided graph:

```python
graph = {
    0: [[1, 4], [2, 1]],
    1: [[3, 1]],
    2: [[1, 2], [3, 5]],
    3: [[4, 3]],
    4: []
}
```

The output of the `lazyDejkstras(graph, 0)` call would be:

```python
{0: 0, 1: 3, 2: 1, 3: 4, 4: 7}
```

This indicates that the shortest distance from node 0 to node 1 is 3, to node 2 is 1, to node 3 is 4, and to node 4 is 7.
