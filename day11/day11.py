from typing import List

import numpy as np
from tqdm import tqdm

def part1(lines: List[str], expansion: int = 2):
    grid_l: List[List[str]] = []
    for line in lines:
        grid_l.append(list(line.strip()))
    grid = np.array(grid_l)
    
    empty_row_indexes = [i for i, row in enumerate(grid) if len(np.unique(row)) == 1]
    empty_column_indexes = [i for i, col in enumerate(grid.T) if len(np.unique(col)) == 1]

    offset = 0
    for row_idx in empty_row_indexes:
        for _ in tqdm(range(expansion - 1)):
            grid = np.insert(grid, row_idx + offset, np.array(["."]*len(grid[row_idx])), axis=0)
            offset += 1

    offset = 0
    for col_idx in empty_column_indexes:
        for _ in tqdm(range(expansion - 1)):
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
    expansion -= 1
    grid_l: List[List[str]] = []
    for line in lines:
        grid_l.append(list(line.strip()))
    grid = np.array(grid_l)
    
    empty_row_indexes = [i for i, row in enumerate(grid) if len(np.unique(row)) == 1]
    empty_column_indexes = [i for i, col in enumerate(grid.T) if len(np.unique(col)) == 1]

    lengths = []
    coords = np.where(grid == "#")
    for v, (i, j) in enumerate(zip(*coords)):
        for w, (x, y) in enumerate(zip(*coords)):
            # Add the amount of empty rows and columns crossed
            rows = sorted([i, x])
            amount_of_rows_crossed = sum([rows[0] <= d <= rows[1] for d in empty_row_indexes])
            columns = sorted([j, y])
            amount_of_cols_crossed = sum([columns[0] <= d <= columns[1] for d in empty_column_indexes])
            distance = sum([abs(i-x), abs(j-y)]) + expansion * amount_of_rows_crossed + expansion * amount_of_cols_crossed
            lengths.append(distance)
            # print(f"{v} {(i, j)} to {w} {x, y}: {distance}")

    return sum(lengths) // 2


if __name__ == "__main__":
    with open("day11/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content, expansion=1000000))