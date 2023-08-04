from collections import deque


def print_dungeon(dungeon: list, L: int, R: int):
    for i in range(L):
        for j in range(R):
            print(" ".join(dungeon[i][j]))

        print("\n")


def input_dungeon(L: int, R: int, C: int) -> list:
    dungeon = [[["." for x in range(C)] for y in range(R)] for z in range(L)]

    for i in range(L):
        for j in range(R):
            for k in range(C):
                dungeon[i][j][k] = input()
                if dungeon[i][j][k] == "S":
                    start = (i, j, k)
                if dungeon[i][j][k] == "E":
                    end = (i, j, k)

    return dungeon, start, end


def solve(
    dungeon: list, start: tuple[int], end: tuple[int], L: int, R: int, C: int
) -> None | int:
    movements = [
        (+1, 0, 0),
        (-1, 0, 0),
        (0, +1, 0),
        (0, -1, 0),
        (0, 0, +1),
        (0, 0, -1),
    ]

    queue = deque()
    queue.append(start)

    visited = set()
    visited.add(start)

    reached_end = False

    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0

    while len(queue) > 0:
        node = queue.popleft()

        if node == end:
            reached_end = True
            break

        for move in movements:
            new_node = (
                node[0] + move[0],
                node[1] + move[1],
                node[2] + move[2],
            )

            if (
                new_node[0] >= L
                or new_node[0] < 0
                or new_node[1] >= R
                or new_node[1] < 0
                or new_node[2] >= C
                or new_node[2] < 0
                or new_node in visited
                or dungeon[new_node[0]][new_node[1]][new_node[2]] == "#"
            ):
                continue

            queue.append(new_node)
            visited.add(new_node)
            nodes_in_next_layer += 1

        nodes_left_in_layer -= 1

        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    if reached_end:
        return move_count
    else:
        return None
    

L = int(input("Enter the number of levels: "))
R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))


while (L != 0) and (R != 0) and (C != 0):
    dungeon, start, end = input_dungeon(L, R, C)

    print_dungeon(dungeon, L, R)
    result = solve(dungeon, start, end, L, R, C)

    if result is not None:
        print(f"The minimum number of moves required to escape: {result}")
    else:
        print("The destination is not reachable.")

    L = int(input("Enter the number of levels: "))
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))


print(dungeon, start, end)
