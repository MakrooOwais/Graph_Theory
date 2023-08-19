const findEularianPath = (graph) => {
    const n = Object.keys(graph).length;
    const m = numEdges(graph);

    const n_in = Array(n).fill(0);
    const n_out = Array(n).fill(0);
    const path = [];

    countInDegrees(graph, n_in, n_out);

    if (!graphHasEularianPath(graph, n_in, n_out)) return null;

    const start = findStartNode(graph, n_in, n_out);

    dfs(graph, start, n_out, path);

    path.unshift(start);

    if (path.length == m + 1) return path;

    return null;
};

const numEdges = (graph) => {
    let num = 0;
    for (let node of Object.keys(graph)) {
        num += graph[node].length;
    }

    return num;
};

const countInDegrees = (graph, n_in, n_out) => {
    for (let node of Object.keys(graph)) {
        for (let edge of graph[node]) {
            n_out[Number(node)]++;
            n_in[Number(edge)]++;
        }
    }
};

const graphHasEularianPath = (graph, n_in, n_out) => {
    const n = Object.keys(graph).length;
    let start_nodes = 0;
    let end_nodes = 0;

    for (let i = 0; i < n; i++) {
        if (Math.abs(n_out[i] - n_in[i]) > 1) return false;
        else if (n_out[i] - n_in[i] === 1) start_nodes++;
        else if (n_in[i] - n_out[i] === 1) end_nodes++;
    }

    return (
        (end_nodes === 0 && start_nodes === 0) ||
        (end_nodes === 1 && start_nodes === 1)
    );
};

const findStartNode = (graph, n_in, n_out) => {
    const n = Object.keys(graph).length;
    let start = 0;

    for (let i = 0; i < n; i++) {
        if (n_out[i] - n_in[i] === 1) return i;

        if (n_out[i] > 0) start = i;
    }

    return start;
};


const dfs = (graph, at, n_out, path) => {
    while (n_out[at] !== 0) {
        n_out[at] -= 1
        let next_edge = graph[String(at)][n_out[at]]

        dfs(graph, next_edge, n_out, path)

        path.unshift(Number(next_edge))
    }
}

const graph = {
    "0": [],
    "1": ["2", "3"],
    "2": ["2", "4", "4"],
    "3": ["1", "2", "5"],
    "4": ["3", "6"],
    "5": ["6"],
    "6": ["3"],
}


console.log(findEularianPath(graph))