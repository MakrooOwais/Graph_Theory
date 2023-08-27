class Edge:
    def __init__(self, origin, to, weight: int = None) -> None:
        self.origin = origin
        self.to = to
        self.weight = weight or 1

    def getRemainingCapacity(self):
        return self.capacity - self.flow

    def __str__(self) -> str:
        return f"{self.origin} -> {self.to} : {self.weight}"


class Graph:
    def __init__(self) -> None:
        self.edges_mat = {}
        self.edges_list = []
        self.edge_list_computed = False

    def addEdge(self, origin, to, weight=  None):
        if origin not in self.edges_mat.keys():
            self.edges_mat[origin] = []
        if to not in self.edges_mat.keys():
            self.edges_mat[to] = []

        e1 = Edge(origin, to, weight)

        self.edges_mat[origin].append(e1)

    def getAdjList(self) -> dict[int:Edge]:
        return self.edges_mat

    def getAdjMat(self) -> list[list[int]]:
        if not self.edge_list_computed:
            node_names = list(self.edges_mat.keys())
            n = len(node_names)

            graph_matrix = [[float("inf") for i in range(n)] for j in range(n)]
            for i in range(n):
                graph_matrix[i][i] = 0

            for node in node_names:
                for edge in self.edges_mat.get(node):
                    origin = node_names.index(edge.origin)
                    to = node_names.index(edge.to)
                    graph_matrix[origin][to] = edge.weight

            self.edge_list_computed = True

        return graph_matrix
