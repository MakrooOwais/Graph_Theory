# Lazy Dijkstra's Algorithm with Shortest Path

Dijkstra's algorithm is a widely used graph traversal algorithm that finds the shortest path from a starting node to all other nodes in a weighted graph. The classic implementation of Dijkstra's algorithm eagerly updates the priority queue to find the shortest distances efficiently. However, the "lazy" version of Dijkstra's algorithm, as shown in the provided Python code, optimizes this process by delaying updates to the priority queue until they are required.

## Lazy Dijkstra's Algorithm

1. Initialize a dictionary `results` with all nodes having a distance of infinity, except for the starting node, which has a distance of 0.

2. Create an empty set `visited` to keep track of the nodes that have been visited.

3. Create a dictionary `prev` to keep track of the previous node in the shortest path for each node. Initialize all values in `prev` to None.

4. Set the distance of the starting node to 0 in the `results` dictionary.

5. Initialize a priority queue `priority_q` with the starting node and its distance as the first element.

6. While the priority queue is not empty, repeat the following steps:
   a. Select the node with the minimum distance from the priority queue using the `min` function with a custom lambda function.
   b. Remove the selected node from the priority queue.
   c. Add the selected node to the `visited` set.

7. Iterate through the neighbors of the selected node:
   a. If the neighbor is already visited, continue to the next neighbor.
   b. If the new distance from the starting node to the neighbor is not better than the current distance, continue to the next neighbor.
   c. Update the distance of the neighbor in the `results` dictionary with the new distance.
   d. Update the previous node for the neighbor in the `prev` dictionary to be the selected node.
   e. Add the neighbor and its updated distance to the priority queue.

8. If the goal is only to find the shortest path between two specific nodes, we can return early as soon as the end node is visited. This optimization can substantially cut the computation time in some cases.

9. Finally, return the `results` dictionary containing the shortest distance from the starting node to all other nodes and the `prev` dictionary containing the previous node in the shortest path for each node.

## Shortest Path Calculation

The provided implementation includes an additional function, `findShortestPath`, to find the actual shortest path between a starting node and an end node after running the lazy Dijkstra's algorithm.

1. Call the `lazyDejkstras` function to get the `results` and `prev` dictionaries.

2. If the shortest distance from the starting node to the end node is `float('inf')`, it means there is no path, so return an empty path.

3. Otherwise, initialize an empty list `path` to store the nodes in the shortest path.

4. Starting from the end node, iterate through the `prev` dictionary to backtrack the shortest path by finding the previous node until reaching the starting node.

5. Insert each node in the path list at the beginning, as we are backtracking from the end to the start.

6. Return the path list containing the shortest path from the starting node to the end node.

## Example

Consider the following graph represented as a dictionary:

```python
graph = {
    0: [[1, 4], [2, 1]],
    1: [[3, 1]],
    2: [[1, 2], [3, 5]],
    3: [[4, 3]],
    4: []
}
```

Using the `findShortestPath` function with `start=0` and `end=4`, we can find the shortest path from node 0 to node 4:

```python
path = findShortestPath(graph, 0, 4)
print(path)
# Output: [0, 2, 1, 3, 4]
```

In this example, the shortest path from node 0 to node 4 is [0, 2, 1, 3, 4]. If the goal is only to find the shortest path between specific nodes, the algorithm will return early as soon as the end node is visited, reducing computation time in some cases.
