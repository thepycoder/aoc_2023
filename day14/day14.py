from typing import Any, List

import numpy as np
from numpy.typing import NDArray
from tqdm import tqdm

def part1(lines: List[str]) -> int:
    grid_l: List[List[str]] = []
    for line in lines:
        grid_l.append(list(line.strip()))
    grid = np.array(grid_l)

    new_stones = simulate_north(grid)
    print(len(lines))
    return sum([len(lines) - x[0] for x in new_stones])

def simulate_north(grid: NDArray[Any]):
    moved = True
    while moved:
        moved = False
        stones = list(zip(*np.where(grid == "O")))
        for stone in stones:
            if stone[0] == 0:
                continue
            to = (stone[0] - 1, stone[1])
            if grid[to] == "#" or grid[to] == "O":
                continue
            grid[to] = "O"
            grid[stone] = "."
            moved = True
    
    new_stones = list(zip(*np.where(grid == "O")))
    return new_stones

def part2(lines: List[str]) -> int:
    grid_l: List[List[str]] = []
    for line in lines:
        grid_l.append(list(line.strip()))
    grid = np.array(grid_l)
    
    cycle_loads: List[int] = []
    # Check for sufficiently long
    for cycle in tqdm(range(1000)):
        for i in range(4):
            # print("\n".join(["".join(row) for row in np.rot90(grid, k=(4-i)%4)]))
            # print("\n\n")
            simulate_north(grid)
            # print(result)
            grid = np.rot90(grid, k=-1)

        new_stones = list(zip(*np.where(grid == "O")))
        cycle_load = sum([len(lines) - x[0] for x in new_stones])
        cycle_loads.append(cycle_load)

    # Calculate the recurring sequence length (stolen function from SO)
    sequence_lentgh = guess_seq_len(cycle_loads[500:])
    print(sequence_lentgh)
    offset = (1000000000 - 500) % sequence_lentgh - 1
    final_load = cycle_loads[500 + offset]
    return final_load

# Straight up stole this from stackoverflow: https://stackoverflow.com/questions/11385718/python-finding-repeating-sequence-in-list-of-integers
def guess_seq_len(seq: List[int]) -> int:
    guess = 1
    max_len = len(seq) // 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            return x

    return guess


if __name__ == "__main__":
    with open("day14/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))