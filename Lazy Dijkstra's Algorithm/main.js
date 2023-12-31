const compareSecondColumn = (a, b) => {
    if (a[1] === b[1]) {
        return 0;
    } else {
        return a[1] < b[1] ? 1 : -1;
    }
};

const lazyDejkkstras = (graph, start) => {
    const results = {};
    const prev = {};
    for ([node, neighbors] of Object.entries(graph)) {
        results[node] = Infinity;
        prev[node] = null;
    }
    visited = new Set();
    results[start] = 0;

    const priority_q = [[start, 0]];

    while (priority_q.length !== 0) {
        node = priority_q.sort(compareSecondColumn).pop();
        visited.add(node[0]);

        for (neighbor of graph[node[0]]) {
            if (!visited.has(neighbor[0])) {
                if (results[neighbor[0]] < results[node[0]] + neighbor[1])
                    continue;
                results[neighbor[0]] = results[node[0]] + neighbor[1];
                prev[neighbor[0]] = node[0];

                priority_q.push([neighbor[0], results[neighbor[0]]]);
            }
        }
    }

    return [results, prev];
};

const findShortestPath = (graph, start, end) => {
    let [n_steps, prev] = lazyDejkkstras(graph, start);
    let path = [];

    if (n_steps[end] === Infinity) return path;

    current_node = end;
    while (current_node !== start) {
        path.unshift(current_node);
        current_node = prev[current_node];
    }

    path.unshift(start);

    return path;
};

const graph_1 = {
    0: [
        ["1", 4],
        ["2", 1],
    ],
    1: [["3", 1]],
    2: [
        ["1", 2],
        ["3", 5],
    ],
    3: [["4", 3]],
    4: [],
};

const graph_2 = {
    0: [
        ["1", 5],
        ["2", 1],
    ],
    1: [
        ["2", 2],
        ["3", 3],
        ["4", 20],
    ],
    2: [
        ["1", 3],
        ["4", 12],
    ],
    3: [
        ["2", 3],
        ["4", 2],
        ["5", 6],
    ],
    4: [["5", 1]],
    5: [],
};

console.log(lazyDejkkstras(graph_1, "0"));
console.log(findShortestPath(graph_1, "0", "4"));
console.log(lazyDejkkstras(graph_2, "0"));
console.log(findShortestPath(graph_2, "0", "5"));
