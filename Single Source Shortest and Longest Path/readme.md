# Single Source Shortest Path (SSSP) and Single Source Longest Path (SSLP) Algorithms

The Single Source Shortest Path (SSSP) and Single Source Longest Path (SSLP) algorithms are used to find the shortest and longest paths, respectively, from a single source vertex to all other vertices in a weighted graph. Both algorithms work with both positive and negative edge weights.

## Algorithm Overview

### Single Source Shortest Path (SSSP)

The SSSP algorithm aims to find the shortest paths from a single source vertex to all other vertices in a weighted graph. It works by iteratively relaxing edges, reducing the distances between vertices until the shortest paths are obtained. The algorithm uses a data structure (such as a priority queue or a min-heap) to efficiently select the next vertex to relax, ensuring that the shortest path to each vertex is calculated in the most optimal way.

### Single Source Longest Path (SSLP)

The SSLP algorithm is similar to the SSSP algorithm but focuses on finding the longest paths from a single source vertex to all other vertices in a weighted graph. The key difference is in how the edges are relaxed. Instead of minimizing the distances, the SSLP algorithm maximizes the distances between vertices by iteratively relaxing the edges.

## Implementation Explanation

The provided Python code demonstrates both the SSSP and SSLP algorithms.

1. `sssp(graph, source)`: This function calculates the Single Source Shortest Path (SSSP) from the given `source` vertex to all other vertices in the weighted graph `graph`. It starts by initializing a `results` dictionary, where each vertex is assigned an initial distance of infinity (`float('inf')`). The distance of the `source` vertex is set to 0, as the distance to itself is 0. The algorithm then iterates over all the vertices and their neighbors, relaxing the edges and updating the distances if a shorter path is found. The function returns the `results` dictionary containing the shortest distances from the `source` vertex to all other vertices.

2. `sslp(graph, source)`: This function calculates the Single Source Longest Path (SSLP) from the given `source` vertex to all other vertices in the weighted graph `graph`. It works similarly to the SSSP algorithm but with the key difference that it initializes the `results` dictionary with negative infinity (`float('-inf')`) instead of positive infinity. The algorithm iterates over all vertices and their neighbors, relaxing the edges and updating the distances if a longer path is found. The function returns the `results` dictionary containing the longest distances from the `source` vertex to all other vertices.

## Example

```python
graph = {
    "a": [["b", 3], ["c", 6]],
    "b": [["c", 4], ["d", 4], ["e", 11]],
    "c": [["d", 8], ["g", 11]],
    "d": [["e", -4], ["f", 5], ["g", 2]],
    "e": [["h", 9]],
    "f": [["h", 1]],
    "g": [["h", 2]],
    "h": [],
}

# Calculate Single Source Shortest Path from vertex 'a'
shortest_path = sssp(graph, 'a')
print("SSSP from 'a':", shortest_path)

# Calculate Single Source Longest Path from vertex 'a'
longest_path = sslp(graph, 'a')
print("SSLP from 'a':", longest_path)
```

The output will show the shortest and longest distances from vertex 'a' to all other vertices in the graph `graph`. The SSSP algorithm will return the shortest path, while the SSLP algorithm will return the longest path.
