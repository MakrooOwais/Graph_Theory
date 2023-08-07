const matrix2list = (graph_matrix, node_num) => {
    const graph_list = {};

    for (let i = 0; i < graph_matrix.length; i++) {
        graph_list[node_num[i]] = [];
    }

    for (let i = 0; i < graph_matrix.length; i++) {
        for (let j = 0; j < graph_matrix.length; j++) {
            if (graph_matrix[i][j] !== 0 && graph_matrix[i][j] !== Infinity) {
                graph_list[node_num[i]].push([node_num[j], graph_matrix[i][j]]);
            }
        }
    }

    return graph_list;
};

const list2matrix = (graph_list) => {
    const node_names = Object.keys(graph_list);
    const n = node_names.length;

    const graph_matrix = Array(n)
        .fill()
        .map(() => Array(n).fill(Infinity));

    for (let i = 0; i < n; i++) {
        graph_matrix[i][i] = 0;
    }

    for (i of node_names) {
        for (j of graph_list[i]) {
            i_ = node_names.indexOf(i);
            j_ = node_names.indexOf(j[0]);
            graph_matrix[i_][j_] = j[1];
        }
    }

    return graph_matrix;
};

const graph_matrix = [
    [0, 4, 1, Infinity],
    [Infinity, 0, 6, Infinity],
    [4, 1, 0, 2],
    [Infinity, Infinity, Infinity, 0],
];

const graph_list = {
    A: [
        ["B", 4],
        ["C", 1],
    ],
    B: [["C", 6]],
    C: [
        ["A", 4],
        ["B", 1],
        ["D", 2],
    ],
    D: [],
};
const node_num = { 0: "A", 1: "B", 2: "C", 3: "D" };

console.log(matrix2list(graph_matrix, node_num));
console.log(list2matrix(graph_list));
