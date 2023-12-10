from collections import deque
from typing import List, Tuple

import numpy as np

VALID_PIPES = {
    "N": ["|", "7", "F"],
    "E": ["-", "7", "J"],
    "S": ["|", "J", "L"],
    "W": ["-", "L", "F"]
}

def get_neighbors(pos: Tuple[int, int], maxi: Tuple[int, int]):
    # Up
    if pos[0] > 0:
        yield "N", (pos[0] - 1, pos[1])
    # Down
    if pos[0] < maxi[0] - 1:
        yield "S", (pos[0] + 1, pos[1])
    # Left
    if pos[1] > 0:
        yield "W", (pos[0], pos[1] - 1)
    # Right
    if pos[1] < maxi[1] - 1:
        yield "E", (pos[0], pos[1] + 1)


def part1(lines: List[str]):
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
        for direction, neighbor in get_neighbors(path[-1], maxi):
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
                return middle
            if grid[neighbor] in VALID_PIPES[direction]:
                new_path.append(neighbor)
                paths.append(new_path)

def part2(lines: List[str]):
    return 0


if __name__ == "__main__":
    with open("day1/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))