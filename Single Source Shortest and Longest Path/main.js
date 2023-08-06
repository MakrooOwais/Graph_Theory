const sssp = (graph, source) => {
    const results = {}
    for ([node, neighbors] of Object.entries(graph)){
        results[node] = Infinity
    }

    results[source] = 0

    for ([node, neighbors] of Object.entries(graph)){
        for (neighbor of neighbors){
            results[neighbor[0]] = Math.min(results[neighbor[0]], results[node] + neighbor[1])
        }
    }

    return results
}

const sslp = (graph, source) => {
    const results = {}
    for ([node, neighbors] of Object.entries(graph)){
        results[node] = -Infinity
    }

    results[source] = 0

    for ([node, neighbors] of Object.entries(graph)){
        for (neighbor of neighbors){
            results[neighbor[0]] = Math.max(results[neighbor[0]], results[node] + neighbor[1])
        }
    }

    return results
}


const graph = {
    "a": [["b", 3], ["c", 6]],
    "b": [["c", 4], ["d", 4], ["e", 11]],
    "c": [["d", 8], ["g", 11]],
    "d": [["e", -4], ["f", 5], ["g", 2]],
    "e": [["h", 9]],
    "f": [["h", 1]],
    "g": [["h", 2]],
    "h": [],
}

console.log(sssp(graph, 'a'))
console.log(sslp(graph, 'a'))