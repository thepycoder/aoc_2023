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

        r_result, c_result, mapping = find_mirror(grid_nr, grid, rows, columns)
        answer_map[mapping[0]] = mapping[1:]
        answers_rows.append(r_result)
        answers_columns.append(c_result)

    return sum(answers_columns) + sum(answers_rows) * 100, answer_map

def find_mirror(grid_nr, grid, rows, columns, old_mapping=None):
    r_result = 0
    c_result = 0
    mapping = (-1, 0, 0)
    for r in range(1, rows):
        mirror_image_size = min(r, abs(r - rows))
        mirrored = np.array_equal(
                grid[r-mirror_image_size:r, :],
                np.flipud(grid[r:r+mirror_image_size, :])
            )
        if mirrored:
            t_mapping = (grid_nr, "r", r)
            if old_mapping:
                if t_mapping[1:] != old_mapping:
                    mapping = t_mapping
                    r_result += r
            else:
                mapping = t_mapping
                r_result += r
        
    for c in range(1, columns):
        mirror_image_size = min(c, abs(c - columns))
        mirrored = np.array_equal(
                grid[:, c-mirror_image_size:c],
                np.fliplr(grid[:, c:c+mirror_image_size]),
            )
        if mirrored:
            # if grid_nr in answer_map:
            #     print("Double mirrorable?")
            t_mapping = (grid_nr, "c", c)
            if old_mapping:
                if t_mapping[1:] != old_mapping:
                    mapping = t_mapping
                    c_result += c
            else:
                mapping = t_mapping
                c_result += c
            
    return r_result, c_result, mapping

def part2(grid_strings: List[str], answer_map: Dict[int, Tuple[str, int]]):
    answer_rows: int = 0
    answer_columns: int = 0
    duplicate_answers = set()
    for grid_nr, grid_s in enumerate(grid_strings):
        grid_l: List[List[str]] = []
        for line in grid_s.strip().split("\n"):
            grid_l.append(list(line.strip()))
        grid = np.array(grid_l)

        rows, columns = grid.shape

        for row in range(rows):
            for column in range(columns):
                prev = grid[row, column]
                grid[row, column] = "." if prev == "#" else "#"
                r_result, c_result, mapping = find_mirror(grid_nr, grid, rows, columns, old_mapping=answer_map[grid_nr])
                grid[row, column] = prev
                if r_result + c_result > 0 and answer_map[grid_nr] != mapping[1:] and mapping not in duplicate_answers:
                    print(f"Found new mirror image! Grid: {grid_nr} -> r{row} c{column} -> {mapping[1:]}")
                    duplicate_answers.add(mapping)
                    if r_result > 0:
                        answer_rows += r_result * 100
                    else:
                        answer_columns += c_result

    return answer_columns + answer_rows


if __name__ == "__main__":
    with open("day13/input.txt", "r") as f:
        content = f.read().split("\n\n")
        result_1, answer_map = part1(content)
        print(result_1)
        print(part2(content, answer_map))