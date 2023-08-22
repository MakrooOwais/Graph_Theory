class Edge:
    def __init__(self, origin, to, flow_capacity, is_residual=False) -> None:
        self.origin = origin
        self.to = to
        self.residual = None
        self.flow_capacity = flow_capacity
        self.flow = 0
        self.is_residual = is_residual

    def setResidual(self, residual):
        self.residual = residual

    def getRemainingCapacity(self):
        return self.flow_capacity - self.flow

    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.flow -= bottleneck

    def __str__(self) -> str:
        return f"{self.origin} -> {self.to} : {self.flow} / {self.flow_capacity}"


class Graph:
    def __init__(self) -> None:
        self.edges = {}

    def addEdge(self, origin, to, capacity):
        if origin not in self.edges.keys():
            self.edges[origin] = []
        if to not in self.edges.keys():
            self.edges[to] = []

        e1 = Edge(origin, to, capacity)
        e2 = Edge(to, origin, 0, True)

        e1.setResidual(e2)
        e2.setResidual(e1)

        self.edges[origin].append(e1)
        self.edges[to].append(e2)

    def getEdges(self) -> dict[int:Edge]:
        return self.edges


SOURCE = 0
SINK = 10


def dfs(graph: Graph, node: int, flow: int, visited: list, visited_token: int):
    if node == SINK:
        return flow

    visited[node] = visited_token

    edges = graph.getEdges().get(node)
    for edge in edges:
        if (edge.getRemainingCapacity() > 0) and (visited[edge.to] != visited_token):
            bottleneck = dfs(
                graph,
                edge.to,
                min(flow, edge.getRemainingCapacity()),
                visited,
                visited_token,
            )

            if bottleneck > 0:
                edge.augment(bottleneck)
                return bottleneck

    return 0


def fordFulkerson(graph: Graph):
    visited_token = 1
    max_flow = 0

    visited = [0] * (len(graph.getEdges()))
    flow = dfs(graph, SOURCE, float("inf"), visited, visited_token)
    visited_token += 1

    while flow != 0:
        max_flow += flow
        flow = dfs(graph, SOURCE, float("inf"), visited, visited_token)
        visited_token += 1

    return max_flow


graph = Graph()

graph.addEdge(0, 1, 10)
graph.addEdge(0, 2, 5)
graph.addEdge(0, 3, 10)
graph.addEdge(1, 4, 10)
graph.addEdge(2, 3, 10)
graph.addEdge(3, 6, 15)
graph.addEdge(4, 2, 20)
graph.addEdge(4, 7, 13)
graph.addEdge(5, 4, 3)
graph.addEdge(5, 2, 15)
graph.addEdge(6, 5, 4)
graph.addEdge(6, 9, 10)
graph.addEdge(7, 8, 10)
graph.addEdge(7, 10, 15)
graph.addEdge(8, 5, 10)
graph.addEdge(8, 6, 7)
graph.addEdge(9, 10, 10)


print(fordFulkerson(graph))
