from typing import List

import numpy as np

def part1(lines: List[str], expansion=1):
    grid_l: List[List[str]] = []
    for line in lines:
        grid_l.append(list(line.strip()))
    grid = np.array(grid_l)
    
    empty_row_indexes = [i for i, row in enumerate(grid) if len(np.unique(row)) == 1]
    empty_column_indexes = [i for i, col in enumerate(grid.T) if len(np.unique(col)) == 1]

    offset = 0
    for row_idx in empty_row_indexes:
        grid = np.insert(grid, row_idx + offset, np.array(["."]*len(grid[row_idx])), axis=0)
        offset += 1

    offset = 0
    for col_idx in empty_column_indexes:
        grid = np.insert(grid, col_idx + offset, np.array(["."]*len(grid.T[col_idx])), axis=1)
        offset += 1

    lengths = []
    coords = np.where(grid == "#")
    for v, (i, j) in enumerate(zip(*coords)):
        for w, (x, y) in enumerate(zip(*coords)):
            distance = sum([abs(i-x), abs(j-y)])
            lengths.append(distance)
            # print(f"{v} {(i, j)} to {w} {x, y}: {distance}")

    return sum(lengths) // 2

def part2(lines: List[str], expansion: int):
    return 0


if __name__ == "__main__":
    with open("day11/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))