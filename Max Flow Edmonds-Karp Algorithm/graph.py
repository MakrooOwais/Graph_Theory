class Edge:
    def __init__(self, origin, to, capacity) -> None:
        self.origin = origin
        self.to = to
        self.residual = None
        self.capacity = capacity
        self.flow = 0

    def setResidual(self, residual):
        self.residual = residual

    def getRemainingCapacity(self):
        return self.capacity - self.flow

    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.flow -= bottleneck

    def is_residual(self):
        return self.capacity == 0

    def __str__(self) -> str:
        return f"{self.origin} -> {self.to} : {self.flow} / {self.capacity}"


class Graph:
    def __init__(self) -> None:
        self.edges_mat = {}
        self.edges_list = []
        self.edge_list_computed = False
        self.max_edge_cap = -float("inf")

    def addEdge(self, origin, to, capacity):
        if origin not in self.edges_mat.keys():
            self.edges_mat[origin] = []
        if to not in self.edges_mat.keys():
            self.edges_mat[to] = []

        self.max_edge_cap = max(self.max_edge_cap, capacity)

        e1 = Edge(origin, to, capacity)
        e2 = Edge(to, origin, 0)

        e1.setResidual(e2)
        e2.setResidual(e1)

        self.edges_mat[origin].append(e1)
        self.edges_mat[to].append(e2)

    def getAdjList(self) -> dict[int:Edge]:
        return self.edges_mat

    def getAdjMat(self) -> list[list[int]]:
        if not self.edge_list_computed:
            node_names = list(self.edges_mat.keys())
            n = len(node_names)

            graph_matrix = [[float("inf") for i in range(n)] for j in range(n)]
            for i in range(n):
                graph_matrix[i][i] = 0

            for node in self.edges_mat.keys():
                for edge in self.edges_mat.get(node):
                    graph_matrix[edge.origin][edge.to] = edge.capacity

            self.edge_list_computed = True

        return graph_matrix
