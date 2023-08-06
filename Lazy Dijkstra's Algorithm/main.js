const compareSecondColumn = (a, b) => {
    if (a[1] === b[1]) {
        return 0;
    } else {
        return a[1] < b[1] ? 1 : -1;
    }
};

const lazyDejkkstras = (graph, start) => {
    const results = {};
    for ([node, neighbors] of Object.entries(graph)) {
        results[node] = Infinity;
    }
    visited = new Set();
    results[start] = 0;

    const priority_q = [[start, 0]];

    while (priority_q.length !== 0) {
        node = priority_q.sort(compareSecondColumn).pop();
        visited.add(node[0]);

        for (neighbor of graph[node[0]]) {
            if (!visited.has(neighbor[0])) {
                results[neighbor[0]] = Math.min(
                    results[node[0]] + neighbor[1],
                    results[neighbor[0]]
                );
                priority_q.push([neighbor[0], results[neighbor[0]]]);
            }
        }
    }

    return results;
};

const graph = {
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


console.log(lazyDejkkstras(graph, "0"));
