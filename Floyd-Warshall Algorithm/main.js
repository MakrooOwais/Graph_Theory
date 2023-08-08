const detectNegativeCycles = (memo, next_node, n) => {
    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (memo[i][j] > memo[i][k] + memo[k][j]) {
                    memo[i][j] = -Infinity;
                    next_node[i][j] = -1;
                }
            }
        }
    }

    return [memo, next_node]
};

const reconstructPath = (memo, next_node, start, end, node_num) => {
    path = [];

    if (memo[start][end] == Infinity) return path;

    let at = start;

    while (at !== end) {
        path.push(node_num[at]);
        at = next_node[at][end];
    }

    if (next_node[at][end] === -1) return null;

    path.push(node_num[end]);

    return path;
};

const floydWarshall = (graph, detectNegativeCycles_B = true) => {
    const n = graph.length;
    const memo = Array(n).fill().map(()=>Array(n).fill(null));
    const next_node = Array(n).fill().map(() => Array(n).fill(null));

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            memo[i][j] = graph[i][j];
            if (memo[i][j] !== Infinity) {
                next_node[i][j] = j;
            }
        }
    }



    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (memo[i][j] > memo[i][k] + memo[k][j]) {
                    memo[i][j] = memo[i][k] + memo[k][j];
                    next_node[i][j] = next_node[i][k];
                }
            }
        }
    }
    if (detectNegativeCycles_B) {
        detectNegativeCycles(memo, next_node, n);
    }

    return [memo, next_node];
};

graph = [
    [0, 4, 1, Infinity],
    [Infinity, 0, 6, Infinity],
    [4, 1, 0, 2],
    [Infinity, Infinity, Infinity, 0],
];

node_num = { 0: "A", 1: "B", 2: "C", 3: "D" };


const [memo, next_node] = floydWarshall(graph)

console.log(memo);
console.log(next_node);

console.log(reconstructPath(memo, next_node, 0, 1, node_num))
