const findBridges = (graph) => {
    const n = Object.keys(graph).length;

    const ids = Array(n).fill(0);
    const low_link = Array(n).fill(0);
    const is_art = Array(n).fill(false)
    const visited = new Set();

    for (let node of Object.keys(graph)) {
        node = Number(node);
        if (!visited.has(node)) {
            out_edges = dfs(graph, node, node, -1, visited, low_link, ids, is_art);
            is_art[node] = out_edges > 1;
        }
    }

    const art_points = []

    for (pos in is_art){
        if (is_art[pos]){
            art_points.push(pos)
        }
    }
    return art_points;
};

const dfs = (
    graph,
    root,
    current_node,
    parent_node,
    visited,
    low_link,
    ids,
    is_art,
    id = 0,
    out_edges =0
) => {
    if (parent_node === root) out_edges++;

    visited.add(current_node);
    id = id + 1;
    low_link[current_node] = ids[current_node] = id;

    for (let neighbor of graph[current_node]) {
        neighbor = Number(neighbor);
        if (neighbor === parent_node) continue;
        if (!visited.has(neighbor)) {
            dfs(graph, root, neighbor, current_node, visited, low_link, ids, is_art, id, out_edges);
            low_link[current_node] = Math.min(low_link[current_node], low_link[neighbor]);
            if (ids[current_node] <= low_link[neighbor]) {
                is_art[current_node] = true
            }
        } else {
            low_link[current_node] = Math.min(low_link[current_node], ids[neighbor]);
        }
    }
    return out_edges;
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
