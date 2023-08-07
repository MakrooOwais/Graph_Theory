def matrix2list(graph_matrix: list, node_num: dict):
    graph_list = {}
    for i in node_num.values():
        graph_list[i] = []

    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix[0])):
            if graph_matrix[i][j] != 0 and graph_matrix[i][j] != float("inf"):
                graph_list[node_num[i]].append([node_num[j], graph_matrix[i][j]])

    return graph_list


def list2matrix(graph_list: dict):
    node_names = list(graph_list.keys())
    n = len(node_names)

    graph_matrix = [[float("inf") for i in range(n)] for j in range(n)]
    for i in range(n):
        graph_matrix[i][i] = 0

    for i in node_names:
        for j in graph_list[i]:
            i_ = node_names.index(i)
            j_ = node_names.index(j[0])
            graph_matrix[i_][j_] = j[1]

    return graph_matrix


graph = [
    [0, 4, 1, float("inf")],
    [float("inf"), 0, 6, float("inf")],
    [4, 1, 0, 2],
    [float("inf"), float("inf"), float("inf"), 0],
]

node_num = {0: "A", 1: "B", 2: "C", 3: "D"}

print(graph)
print(matrix2list(graph, node_num))
