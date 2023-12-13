import time
from typing import Dict, List, Tuple

import numpy as np

def part1(grid_strings: List[str]):
    answers_rows: List[int] = []
    answers_columns: List[int] = []
    answer_map: Dict[int, Tuple[str, int]] = dict()
    for grid_nr, grid_s in enumerate(grid_strings):
        grid_l: List[List[str]] = []
        for line in grid_s.strip().split("\n"):
            grid_l.append(list(line.strip()))
        grid = np.array(grid_l)

        rows, columns = grid.shape

        for r in range(1, rows):
            mirror_image_size = min(r, abs(r - rows))
            mirrored = np.array_equal(
                grid[r-mirror_image_size:r, :],
                np.flipud(grid[r:r+mirror_image_size, :])
            )
            if mirrored:
                if grid_nr in answer_map:
                    print("Double mirrorable?")
                answer_map[grid_nr] = ("r", r)
                answers_rows.append(r)
        
        for c in range(1, columns):
            mirror_image_size = min(c, abs(c - columns))
            mirrored = np.array_equal(
                grid[:, c-mirror_image_size:c],
                np.fliplr(grid[:, c:c+mirror_image_size]),
            )
            if mirrored:
                if grid_nr in answer_map:
                    print("Double mirrorable?")
                answer_map[grid_nr] = ("c", c)
                answers_columns.append(c)

    return sum(answers_columns) + sum(answers_rows) * 100, answer_map

def part2(grid_strings: List[str], answer_map: Dict[int, Tuple[str, int]]):

    return 0


if __name__ == "__main__":
    with open("day13/input.txt", "r") as f:
        content = f.read().split("\n\n")
        result_1, answer_map = part1(content)
        print(result_1)
        print(part2(content))