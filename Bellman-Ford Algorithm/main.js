const bellmanFord = (graph, start) => {
    const result = {};

    for (let i in graph) {
        result[i] = Infinity
    }

    result[start] = 0

    for (let node in graph){
        for (let neighbor of graph[node]){
            result[neighbor[0]] = Math.min(result[neighbor[0]], result[node] + neighbor[1]) 
        }
    }

    for (let i = 0; i < Object.keys(graph).length - 1; i++){
        for (let node in graph){
            for (let neighbor of graph[node]){
                if (result[neighbor[0]] >  result[node] + neighbor[1]) {
                    result[neighbor[0]] = -Infinity
                }
            }
        }
    }

    console.log(result)
};


graph = {
    0: [["1", 5]],
    1: [
        ["2", 20],
        ["5", 30],
        ["6", 60],
    ],
    2: [
        ["3", 10],
        ["4", 75],
    ],
    3: [["2", -15]],
    4: [["9", 100]],
    5: [
        ["4", 25],
        ["6", 5],
        ["8", 50],
    ],
    6: [["7", -50]],
    7: [["8", -10]],
    8: [],
    9: [],
};

bellmanFord(graph, "0");
