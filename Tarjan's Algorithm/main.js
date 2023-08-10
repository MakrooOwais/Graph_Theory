const findSSCs = (graph) => {
    n = Object.keys(graph).length;

    const visited = new Set();
    const low_link = Array(n).fill(Infinity);
    let sccs = Array()

    for (let i in graph) {
        i = Number(i);
        sccs = dfs(graph, i, low_link, visited, sccs);
    }

    return sccs;
};

const dfs = (graph, node, low_link, visited, sccs = Array(), stack = []) => {
    visited.add(node);
    stack.push(node);
    low_link[node] = node;

    for (let neighbor of graph[node]) {
        if (!visited.has(neighbor)) {
            dfs(graph, neighbor, low_link, visited, sccs, stack);
        }
        
        
        if (stack.includes(neighbor)) {
            low_link[node] = Math.min(low_link[neighbor], low_link[node]);
        }
    }

    if (node === low_link[node]) {
        if (stack.length > 1) {
            const scc = [];
            while (true) {
                let stack_node = stack.pop();
                scc.unshift(stack_node);
                low_link[stack_node] = node;
                if (stack_node === node) {
                    if (scc.length > 1) {
                        sccs.push(scc);
                    }
                    break;
                }
            }
            
        }
    }

    return sccs;
};

graph = {
    0: [1],
    1: [2],
    2: [0],
    3: [4, 7],
    4: [5],
    5: [0, 6],
    6: [0, 2, 4],
    7: [3, 5],
};

console.log(findSSCs(graph));
