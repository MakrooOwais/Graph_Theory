# Eager Dijkstra's Algorithm and Shortest Path Calculation

## Eager Dijkstra's Algorithm

Dijkstra's algorithm is a well-known graph traversal algorithm that efficiently finds the shortest path from a starting node to all other nodes in a weighted graph. The eager implementation of Dijkstra's algorithm eagerly updates the priority queue as soon as a shorter path to a node is found, ensuring that the shortest distances are maintained at all times.

## Eager Dijkstra's Algorithm - Implementation

The provided Python code demonstrates the eager implementation of Dijkstra's algorithm:

1. Initialize a dictionary `results` with all nodes having a distance of infinity, except for the starting node, which has a distance of 0.

2. Create an empty set `visited` to keep track of the nodes that have been visited.

3. Create a dictionary `prev` to keep track of the previous node in the shortest path for each node. Initialize all values in `prev` to None.

4. Set the distance of the starting node to 0 in the `results` dictionary.

5. Initialize a priority queue `priority_q` as a dictionary with the starting node and its distance as the first key-value pair.

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

8. The algorithm returns two dictionaries: `results` containing the shortest distance from the starting node to all other nodes, and `prev` containing the previous node in the shortest path for each node.

## Shortest Path Calculation

The `findShortestPath` function utilizes the eager implementation of Dijkstra's algorithm to find the actual shortest path between a starting node and an end node.

1. Call the `eagerDejkstras` function to get the `results` and `prev` dictionaries.

2. If the shortest distance from the starting node to the end node is `float('inf')`, it means there is no path, so return an empty path.

3. Otherwise, initialize an empty list `path` to store the nodes in the shortest path.

4. Starting from the end node, iterate through the `prev` dictionary to backtrack the shortest path by finding the previous node until reaching the starting node.

5. Insert each node in the path list at the beginning, as we are backtracking from the end to the start.

6. Return the path list containing the shortest path from the starting node to the end node.

## Difference between Lazy and Eager Dijkstra's Algorithm

The main difference between the lazy and eager implementations of Dijkstra's algorithm lies in how they handle priority queue updates:

1. Eager Dijkstra's Algorithm:
   - The eager implementation eagerly updates the priority queue with new distances whenever a shorter path is found to a node.
   - This ensures that the priority queue always contains the most up-to-date distances and allows the algorithm to find the shortest path efficiently.

2. Lazy Dijkstra's Algorithm (Previous Implementation):
   - The lazy implementation delays the priority queue updates until they are required, resulting in fewer updates to the queue.
   - This can potentially save computation time, especially in cases where many nodes have similar distances and multiple updates are not necessary.

Both implementations yield the same results, finding the shortest path from a starting node to all other nodes. The choice between the eager and lazy implementation depends on the specific characteristics of the graph and the desired performance trade-offs.
