# Conversion Between Graph Representations

This Python script provides two functions to convert a graph between two common representations: adjacency matrix and adjacency list.

## `matrix2list`

The `matrix2list` function takes an adjacency matrix `graph_matrix` and a `node_num` dictionary that maps node indices to corresponding node labels or identifiers. It converts the graph from an adjacency matrix representation to an adjacency list representation. The resulting `graph_list` is a dictionary, where each key is a node identifier, and the corresponding value is a list of neighbor nodes with their edge weights.

## `list2matrix`

The `list2matrix` function takes an adjacency list `graph_list` as input. It converts the graph from an adjacency list representation to an adjacency matrix representation. The resulting `graph_matrix` is a 2D list, where the value at index (i, j) represents the weight of the edge between nodes i and j. If there is no edge between two nodes, the weight is set to `float("inf")`.

## Example

Given the input graph in the form of an adjacency matrix:

```python
graph = [
    [0, 4, 1, float("inf")],
    [float("inf"), 0, 6, float("inf")],
    [4, 1, 0, 2],
    [float("inf"), float("inf"), float("inf"), 0],
]

node_num = {0: "A", 1: "B", 2: "C", 3: "D"}
```

1.Converting the adjacency matrix to an adjacency list:

```python
graph_list = matrix2list(graph, node_num)
```

The resulting `graph_list` will be:

```python
{
    "A": [["B", 4], ["C", 1]],
    "B": [["C", 6]],
    "C": [["A", 4], ["B", 1], ["D", 2]],
    "D": []
}
```

2.Converting the adjacency list back to an adjacency matrix:

```python
graph_matrix = list2matrix(graph_list)
```

The resulting `graph_matrix` will be:

```python
[
    [0, 4, 1, inf],
    [inf, 0, 6, inf],
    [4, 1, 0, 2],
    [inf, inf, inf, 0]
]
```

The functions `matrix2list` and `list2matrix` can be useful when working with graph algorithms that require different graph representations. By converting the graph between these two representations, you can choose the most suitable one for your specific algorithm or application.
