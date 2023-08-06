const depthFirstSearch = (graph, current_node, visited, nodes) => {
    visited.add(current_node);

    connected_nodes = graph[current_node];

    for (let dest_node of connected_nodes) {
        if (!visited.has(dest_node)) {
            depthFirstSearch(graph, dest_node, visited, nodes);
        }
    }

    nodes.unshift(current_node);
};

const topologicalSort = (graph) => {
    let visited = new Set();
    let ordering = [];

    for (let node of Object.entries(graph)) {
        node = node[0];
        if (!visited.has(node)) {
            depthFirstSearch(graph, node, visited, ordering);
        }
    }
    return ordering;
};

const graph = {
    a: ["d"],
    b: ["d"],
    c: ["a", "b"],
    d: ["g", "h"],
    e: ["a", "d", "f"],
    f: ["k", "j"],
    g: ["i"],
    h: ["i", "j"],
    i: ["l"],
    j: ["m", "l"],
    k: ["j"],
    l: [],
    m: [],
};

console.log(topologicalSort(graph));
