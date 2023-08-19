# Eulerian Path in a Graph - Problem Statement

The **Eulerian Path** is a fundamental concept in graph theory that refers to a path in a graph that visits every edge exactly once. It is named after the Swiss mathematician Leonhard Euler, who solved the famous Seven Bridges of Königsberg problem, a precursor to the Eulerian Path problem. An **Eulerian Path** may or may not start and end at the same vertex.

## Problem Statement

Given a directed graph, the goal of the Eulerian Path problem is to find a path that traverses each edge exactly once, if such a path exists.

### Input

- **Graph Representation**: The graph is represented as a dictionary, where each vertex is a key, and its value is a list of vertices to which it has directed edges.

### Output

- **Eulerian Path**: A sequence of vertices that forms an Eulerian Path in the given graph, if it exists. If no Eulerian Path exists, return `None`.

## Eulerian Paths and Graph Properties

The existence of an Eulerian Path in a graph depends on certain properties:

- **Semi-Eulerian Graph**: A graph has a semi-Eulerian path if there are exactly two vertices with (outdegree - indegree) = 1 and (indegree - outdegree) = 1, and all other vertices have equal in-degree and out-degree.

- **Eulerian Graph**: A graph has an Eulerian cycle if every vertex has equal in-degree and out-degree, and the graph is strongly connected (all vertices are reachable from any other vertex).

- **Eulerian Path**: A graph has an Eulerian path if all vertices have equal in-degree and out-degree except for two vertices, one with (outdegree - indegree) = 1 and the other with (indegree - outdegree) = 1.

## Algorithm Implementation

The provided Python code implements the Eulerian Path algorithm using the following functions:

- `num_edges(graph: dict) -> int`: Counts the total number of edges in the graph.
- `countInOutDegrees(graph: dict, n_in: list[int], n_out: list[int])`: Counts the in-degrees and out-degrees for each vertex.
- `graphHasEularianPath(graph: dict, n_in: list[int], n_out: list[int]) -> bool`: Checks whether the given graph has an Eulerian Path.
- `findStartNode(graph: dict, n_in: list[int], n_out: list[int])`: Finds the starting vertex for the Eulerian Path.
- `dfs(graph: dict, at: int, n_out: list[int], path: list)`: Performs a depth-first search to find the Eulerian Path.

## Example

Consider the following directed graph:

```pyhton
{
    "0": [],
    "1": ["2", "3"],
    "2": ["2", "4", "4"],
    "3": ["1", "2", "5"],
    "4": ["3", "6"],
    "5": ["6"],
    "6": ["3"],
}
```

The Eulerian Path for this graph is `1 -> 3 -> 5 -> 6 -> 3 -> 2 -> 4 -> 3 -> 1 -> 2 -> 2 -> 4 -> 6`, which traverses each edge exactly once.

## Conclusion

The Eulerian Path problem is a fascinating area of graph theory that has numerous applications in computer science, transportation, circuit design, and more. The provided algorithm offers an effective way to find Eulerian Paths in directed graphs by considering the properties of in-degrees and out-degrees of vertices. It's important to note that not all graphs have Eulerian Paths, and the algorithm provides a method to verify their existence.
