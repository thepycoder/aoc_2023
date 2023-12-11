from collections import deque
from typing import List, Set, Tuple

import numpy as np
from numpy.typing import NDArray

VALID_PIPES = {
    "N": ["S", "|", "7", "F"],
    "E": ["S", "-", "7", "J"],
    "S": ["S", "|", "J", "L"],
    "W": ["S", "-", "L", "F"]
}

CROSSED_PIPES = {
    "V": ["S", "-", "7", "F", "J", "L"],
    "H": ["S", "|", "7", "J", "L", "F"],
}


def get_neighbors(grid: NDArray[np.int32], pos: Tuple[int, int], maxi: Tuple[int, int]):
    # Up
    if grid[pos] in VALID_PIPES["S"] and pos[0] > 0:
        yield "N", (pos[0] - 1, pos[1])
    # Down
    if grid[pos] in VALID_PIPES["N"] and pos[0] < maxi[0] - 1:
        yield "S", (pos[0] + 1, pos[1])
    # Left
    if grid[pos] in VALID_PIPES["E"] and pos[1] > 0:
        yield "W", (pos[0], pos[1] - 1)
    # Right
    if grid[pos] in VALID_PIPES["W"] and pos[1] < maxi[1] - 1:
        yield "E", (pos[0], pos[1] + 1)


def part1(lines: List[str]) -> Tuple[List[Tuple[int, int]], int]:
    grid_l: List[List[str]] = []
    for line in lines:
        grid_l.append(list(line))
    grid = np.array(grid_l)
    maxi: Tuple[int, int] = (grid.shape[0], grid.shape[1])
    start_pos = np.where(grid == "S")

    paths: deque[List[Tuple[int, int]]] = deque()
    paths.append([(start_pos[0][0], start_pos[1][0])])

    searching = True
    while searching:
        path = paths.popleft()
        for direction, neighbor in get_neighbors(grid, path[-1], maxi):
            new_path = path.copy()
            if len(new_path) >= 2 and neighbor == new_path[-2]:
                # Don't go backwards!
                continue
            if grid[neighbor] == "S":
                print("We be loopin!")
                print(new_path)
                print(neighbor)
                new_path.append(neighbor)
                middle = len(new_path) // 2
                furthest_point = new_path[middle]
                print(furthest_point)
                searching = False
                return new_path, middle
            if grid[neighbor] in VALID_PIPES[direction]:
                new_path.append(neighbor)
                paths.append(new_path)
    raise ValueError("This means there is no solution found?")


def replace_horizontal(chunk: str):
    chunk = chunk.replace("LJ", "||")
    chunk = chunk.replace("F7", "||")
    chunk = chunk.replace("FJ", "|")
    chunk = chunk.replace("L7", "|")
    return chunk


def replace_vertical(chunk: str):
    chunk = chunk.replace("7J", "--")
    chunk = chunk.replace("FL", "--")
    chunk = chunk.replace("7L", "-")
    chunk = chunk.replace("FJ", "-")
    return chunk


def part2(lines: List[str], loop: Set[Tuple[int, int]]):
    grid_l: List[List[str]] = []
    for line in lines:
        grid_l.append(list(line))
    grid = np.array(grid_l)
    # maxi: Tuple[int, int] = (grid.shape[0], grid.shape[1])
    # display_grid = grid.copy()

    total = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # If part of the loop, skip, can't be inside or outside
            if (i, j) in loop:
                continue

            # Use raycasting algorithm to determine if point is inside or outside of loop
            # Note to self: read the entire algorithm description. You only need to cast 1 ray per point
            # Cast left
            # left_coordinates = [(i, x) for x in range(j) if grid[i, x] in CROSSED_PIPES["H"]]
            # s = len(set(left_coordinates).intersection(loop))
            left_coordinates = [(i, x) for x in range(j) if grid[i, x] != "-"]
            left_chunks = "".join([" " if c not in loop else grid[c] for c in left_coordinates]).split()
            left_chunks = [replace_horizontal(u) for u in left_chunks]
            s = sum([len(c) for c in left_chunks])
            if s % 2 == 0:
                continue
            # Cast right
            # right_coordinates = [(i, x) for x in range(j, maxi[1]) if grid[i, x] in CROSSED_PIPES["H"]]
            # s = len(set(right_coordinates).intersection(loop))
            # right_coordinates = [(i, x) for x in range(j, maxi[1]) if grid[i, x] != "-"]
            # right_chunks = "".join([" " if c not in loop else grid[c] for c in right_coordinates]).split()
            # right_chunks = [replace_horizontal(u) for u in right_chunks]
            # s = sum([len(c) for c in right_chunks])
            # if s % 2 == 0:
            #     continue
            # # Cast up
            # # up_coordinates = [(x, j) for x in range(i) if grid[x, j] in CROSSED_PIPES["V"]]
            # # s = len(set(up_coordinates).intersection(loop))
            # up_coordinates = [(x, j) for x in range(i) if grid[x, j] != "|"]
            # up_chunks = "".join([" " if c not in loop else grid[c] for c in up_coordinates]).split()
            # up_chunks = [replace_vertical(u) for u in up_chunks]
            # s = sum([len(c) for c in up_chunks])
            # if s % 2 == 0:
            #     continue
            # # Cast down
            # # down_coordinates = [(x, j) for x in range(i, maxi[0]) if grid[x, j] in CROSSED_PIPES["V"]]
            # # s = len(set(down_coordinates).intersection(loop))
            # down_coordinates = [(x, j) for x in range(i, maxi[0]) if grid[x, j] != "|"]
            # down_chunks = "".join([" " if c not in loop else grid[c] for c in down_coordinates]).split()
            # down_chunks = [replace_vertical(u) for u in down_chunks]
            # s = sum([len(c) for c in down_chunks])
            # if s % 2 == 0:
            #     continue

            # print(f"{(i, j)} is IN!")
            # display_grid[i, j] = "#"
            total += 1
    # print("\n".join(["".join(row) for row in display_grid]))
    return total



if __name__ == "__main__":
    with open("day10/input.txt", "r") as f:
        content = f.readlines()
        loop, distance = part1(content)
        print(distance)
        print(part2(content, set(loop)))