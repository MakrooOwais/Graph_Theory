# Floyd-Warshall Algorithm for All-Pairs Shortest Paths

This Python script implements the Floyd-Warshall algorithm, an efficient algorithm for finding the shortest paths between all pairs of nodes in a weighted graph. The script also provides functions to detect negative cycles in the graph and to reconstruct the shortest path between two nodes.

## `floydWarshall`

The `floydWarshall` function takes a weighted graph represented as an adjacency matrix `graph` as input. It returns two tables: -`memo`: A 2D list that represents the shortest distances between all pairs of nodes. `memo[i][j]` contains the shortest distance from node `i` to node `j`. -`next_node`: A 2D list that stores information on the next node in the shortest path from `i` to `j`. `next_node[i][j]` contains the next node in the path from `i` to `j`.

## `detectNegativeCycles`

The `detectNegativeCycles` function is used to detect negative cycles in the graph using the Floyd-Warshall algorithm. It takes the `memo` and `next_node` tables and the number of nodes `n` in the graph as inputs. If there is a negative cycle in the graph, this function marks the corresponding entries in the `memo` table as `-infinity` and sets the `next_node` table entries to `-1`.

## `reconstructPath`

The `reconstructPath` function reconstructs the shortest path between two nodes (`start` and `end`) in the graph using the `memo` and `next_node` tables. It takes the `memo` and `next_node` tables, the node identifiers `node_num`, and the starting and ending nodes as inputs. If there is no valid path between the two nodes, it returns an empty path. If a negative cycle exists in the graph, it returns `None` to indicate that no valid path exists.

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

1.Running the `floydWarshall` function:

```python
memo, next_node = floydWarshall(graph)
```

The resulting `memo` and `next_node` tables will be:

```python
memo = [
    [0, 3, 1, 3],
    [float("inf"), 0, 4, 6],
    [3, 1, 0, 2],
    [float("inf"), float("inf"), float("inf"), 0]
]

next_node = [
    [0, 2, 2, 2],
    [None, 1, 2, 2],
    [1, 1, 2, 3],
    [None, None, None, 3]
]
```

2.Reconstructing the shortest path between nodes A (0) and B (1):

```python
path = reconstructPath(memo, next_node, 0, 1, node_num)
print(path)
```

The output will be:

```python
['A', 'C', 'B']
```

This indicates that the shortest path from node A to node B is A -> C -> B with a total distance of 3.
