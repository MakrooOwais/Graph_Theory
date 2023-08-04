# The Dungeon Problem

You are trapped in a 3D dungeon and need to find the quickest way out! The dungeon is composed of unit cubes which may or may not be filled with rock. It takes one minute to move one unit north, south, east, west, up or down. You cannot move diagonally and the maze is surrounded by solid rock on all sides.

Is an escape possible? If yes, how long will it take?

## Input Specification

The input file consists of a number of dungeons. Each dungeon description starts with a line containing three integers `L`, `R`, and `C` (all limited to 30 in size). `L` is the number of levels making up the dungeon. `R` and `C` are the number of rows and columns making up the plan of each level.

Then there will follow `L` blocks of `R` lines each containing `C` characters. Each character describes one cell of the dungeon. A cell full of rock is indicated by a `#` and empty cells are represented by a `.`. Your starting position is indicated by `S` and the exit by the letter `E`. There’s a single blank line after each level. Input is terminated by three zeroes for `L`, `R` and `C`.

## Output Specification

Each maze generates one line of output. If it is possible to reach the exit, print a line of the form:
`Escaped in <x> minute(s).`
where `<x>` is replaced by the shortest time it takes to escape. If it is not possible to escape, print the line
`Trapped!`

## Sample Input 1

```text
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

1 3 3
S##
#E#
###

0 0 0
```

## Sample Output 1

```pyhton
The minimum number of moves required to escape: 11
The destination is not reachable.
```

# Dungeon Escape

The provided Python code is an implementation of a dungeon escape algorithm using Breadth-First Search (BFS). The dungeon is represented as a 3D grid, where each cell can be either empty (denoted by ".") or blocked (denoted by "#"). The player's starting position is marked by "S," and the destination is marked by "E."

## Function: print_dungeon(dungeon, L, R)

This function takes a 3D dungeon grid (`dungeon`) and its dimensions (`L` - number of levels and `R` - number of rows) as input. It prints the dungeon layout by displaying each level of the grid with each row separated by a new line.

## Function: input_dungeon(L, R, C) -> (dungeon, start, end)

This function takes the dimensions of the dungeon (`L`, `R`, `C`) as input and allows the user to input the dungeon layout interactively. The user is prompted to enter the character for each cell in the grid, and the "S" and "E" positions are stored as the starting and destination positions, respectively. The function returns the constructed dungeon grid, the start position, and the end position.

## Function: solve(dungeon, start, end, L, R, C) -> int | None

This function takes the dungeon grid (`dungeon`), start position (`start`), end position (`end`), and the dimensions of the grid (`L`, `R`, `C`) as input. It uses BFS to find the minimum number of moves required to reach the destination from the starting position.

The function initializes a queue and starts the BFS by exploring the neighbors of the starting position. It keeps track of visited cells using a set (`visited`) to avoid revisiting the same cell multiple times. The BFS continues until it reaches the destination cell (marked "E") or explores all reachable cells without finding the destination. If the destination cell is reached, the function returns the minimum number of moves required to reach the destination. Otherwise, it returns `None`, indicating that the destination is not reachable.

## Main Program

The main program takes the dimensions of the dungeon (`L`, `R`, `C`) as input. It then repeatedly inputs the dungeon layout and finds the minimum number of moves required to escape from the starting position (S) to the destination (E) using the `solve` function. The program stops when the dimensions of the dungeon are all zeros.

Note: The last line `print(dungeon, start, end)` appears to be an attempt to print the dungeon layout, start, and end positions outside the loop. However, it will not work as the variables `dungeon`, `start`, and `end` are only accessible within the loop's scope.

## Example Usage

```python
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
```

This code allows the user to input the dimensions and layout of a dungeon interactively and find the minimum number of moves required to escape from the starting position (S) to the destination (E). The program repeats this process until the user enters all zeros for the dungeon dimensions.
