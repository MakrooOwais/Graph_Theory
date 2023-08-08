const findBridges = (graph) => {
    const n = Object.keys(graph).length;

    const ids = Array(n).fill(0);
    const low_link = Array(n).fill(0);
    const visited = new Set();

    for (let node of Object.keys(graph)) {
        node = Number(node);
        if (!visited.has(node)) {
            bridges = dfs(graph, node, -1, visited, low_link, ids);
        }
    }

    return bridges;
};

const dfs = (
    graph,
    node,
    parent_node,
    visited,
    low_link,
    ids,
    id = 0,
    bridges = []
) => {
    visited.add(node);
    id = id + 1;
    low_link[node] = ids[node] = id;

    for (let neighbor of graph[node]) {
        neighbor = Number(neighbor);
        if (neighbor === parent_node) continue;
        if (!visited.has(neighbor)) {
            dfs(graph, neighbor, node, visited, low_link, ids, id, bridges);
            low_link[node] = Math.min(low_link[node], low_link[neighbor]);
            if (ids[node] < low_link[neighbor]) {
                bridges.push([node, neighbor]);
            }
        } else {
            low_link[node] = Math.min(low_link[node], ids[neighbor]);
        }
    }
    return bridges;
};

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 8],
    6: [5, 7],
    7: [6, 8],
    8: [5, 7],
};

console.log(findBridges(graph));
