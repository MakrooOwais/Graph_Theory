# Bellman-Ford Algorithm

The Bellman-Ford algorithm is a popular algorithm for finding the shortest path from a single source vertex to all other vertices in a weighted graph. It is applicable to graphs that may have negative edge weights but does not handle negative cycles.

## Algorithm Steps

1. Initialize the result dictionary to store the shortest distances from the source vertex to all other vertices. Set the distance of the source vertex to itself as 0 and the distances to all other vertices as infinity.

2. Relaxation Step: Iterate through each vertex in the graph for a total of (V - 1) times, where V is the number of vertices in the graph. For each vertex, examine all its outgoing edges, and if the distance to a neighboring vertex can be reduced by considering the current vertex as an intermediate node, update the distance accordingly.

3. Negative Cycle Detection: After (V - 1) iterations, check for any further reductions in the distances in the Relaxation Step. If any such reductions occur, it indicates the presence of a negative cycle in the graph. In this case, the algorithm stops and returns a result indicating that there is no unique shortest path.

4. Return the final result dictionary containing the shortest distances from the source vertex to all other vertices.

## Implementation Explanation

The provided Python function `bellmanFord` takes a weighted graph represented as a dictionary as input and returns a dictionary with the shortest distances from the specified source vertex to all other vertices.

The function follows the steps of the Bellman-Ford algorithm:

1. The `result` dictionary is initialized, and the distance of the source vertex to itself is set to 0, and the distances to all other vertices are set to infinity.

2. The Relaxation Step is performed in a nested loop. The outer loop iterates through all the vertices in the graph, and the inner loop iterates through all the neighboring vertices of the current vertex. If the distance to a neighboring vertex can be reduced by considering the current vertex as an intermediate node, the distance is updated in the `result` dictionary.

3. The Negative Cycle Detection is achieved by iterating through the graph vertices one more time. If any distance can still be reduced, it means there is a negative cycle, and the distance for that vertex is set to negative infinity.

4. Finally, the `result` dictionary containing the shortest distances from the source vertex to all other vertices is returned.

## Example

Consider the given graph:

```python
graph = {
    "0": [["1", 5]],
    "1": [["2", 20], ["5", 30], ["6", 60]],
    "2": [["3", 10], ["4", 75]],
    "3": [["2", -15]],
    "4": [["9", 100]],
    "5": [["4", 25], ["6", 5], ["8", 50]],
    "6": [["7", -50]],
    "7": [["8", -10]],
    "8": [],
    "9": [],
}
```

When calling `bellmanFord(graph, '0')`, the algorithm calculates the shortest distances from vertex '0' to all other vertices. The result dictionary will contain:

```python
{
    '0': 0,
    '1': 5,
    '2': -float('inf'),
    '3': -float('inf'),
    '4': -float('inf'),
    '5': 35,
    '6': 40,
    '7': -10,
    '8': -20,
    '9': -float('inf')
}
```

In this case, the algorithm detected a negative cycle in the graph, resulting in some vertices having distances set to negative infinity.

**Note**: In the provided implementation, the negative cycle detection step sets the distances of vertices with negative cycles to negative infinity. This can be adjusted based on the specific use case to fit the application's needs.
