const printDungeon = (dungeon, L, R) => {
    for (let i = 0; i < L; i++) {
        for (let j = 0; j < R; j++) {
            console.log(dungeon[i][j].join(" "));
        }
        console.log("\n");
    }
};

const inputDungeon = (L, R, C) => {
    dungeon = Array(L)
        .fill()
        .map(() =>
            Array(R)
                .fill()
                .map(() => Array(C).fill("."))
        );

    const prompt = require("prompt-sync")({ sigint: true });
    for (let i = 0; i < L; i++) {
        for (let j = 0; j < R; j++) {
            for (let k = 0; k < C; k++) {
                dungeon[i][j][k] = prompt();
                if (dungeon[i][j][k] === "S") {
                    const start = [i, j, k];
                }
                if (dungeon[i][j][k] === "E") {
                    const end = [i, j, k];
                }
            }
        }
    }

    return dungeon, start, end;
};

const solve = (dungeon, start, end, L, R, C) => {
    const movements = [
        [+1, 0, 0],
        [-1, 0, 0],
        [0, +1, 0],
        [0, -1, 0],
        [0, 0, +1],
        [0, 0, -1],
    ];

    let queue = [start];

    let visited = new Set();
    visited.add(start.join(" "));

    let reached_end = false;

    let move_count = 0;
    let nodes_left_in_layer = 1;
    let nodes_in_next_layer = 0;

    while (queue.length > 0) {
        let node = queue.shift();

        if (node.join(" ") === end.join(" ")) {
            reached_end = true;
            break;
        }

        for (let move of movements) {
            let new_node = [
                node[0] + move[0],
                node[1] + move[1],
                node[2] + move[2],
            ];

            if (
                new_node[0] >= L ||
                new_node[0] < 0 ||
                new_node[1] >= R ||
                new_node[1] < 0 ||
                new_node[2] >= C ||
                new_node[2] < 0 ||
                visited.has(new_node.join(" ")) ||
                dungeon[new_node[0]][new_node[1]][new_node[2]] === "#"
            ) {
                continue;
            }

            queue.push(new_node);
            visited.add(new_node.join(" "));
            nodes_in_next_layer++;
        }

        nodes_left_in_layer--;

        if (nodes_left_in_layer === 0) {
            nodes_left_in_layer = nodes_in_next_layer;
            nodes_in_next_layer = 0;
            move_count++;
        }
    }

    if (reached_end) {
        return move_count;
    } else {
        return null;
    }
};

const dungeon = [
    [
        ["S", ".", ".", ".", "."],
        [".", "#", "#", "#", "."],
        [".", "#", "#", ".", "."],
        ["#", "#", "#", ".", "#"],
    ],
    [
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", "#", ".", "#", "#"],
        ["#", "#", ".", ".", "."],
    ],
    [
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", ".", "#", "#", "#"],
        ["#", "#", "#", "#", "E"],
    ],
];

const start = [0, 0, 0];
const end = [2, 3, 4];

printDungeon(dungeon, 3, 4);
result = solve(dungeon, start, end, 3, 4, 5);


if (result !== null){
    console.log(`The minimum number of moves required to escape: ${result}`)
}
    else{
        console.log("The destination is not reachable.")
    }

