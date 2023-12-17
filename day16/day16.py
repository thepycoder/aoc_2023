from collections import deque
from copy import copy, deepcopy
from dataclasses import dataclass
from hashlib import new
from typing import List, Sequence, Set

import numpy as np
from numpy.typing import NDArray


@dataclass
class Tile:
    coords: NDArray[np.int32]
    incoming_direction: str

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Tile):
            return (
                self.incoming_direction == other.incoming_direction
                and np.array_equal(self.coords, other.coords)
            )
        return False

    def __hash__(self) -> int:
        return hash(self.coords.tostring().decode() + self.incoming_direction)


@dataclass
class Beam:
    path: List[Tile]

direction_to_coord = {
    "r": np.array([0, 1]),
    "l": np.array([0, -1]),
    "u": np.array([-1, 0]),
    "d": np.array([1, 0]),
}

direction_effect_mapping = {
    "r/": ["u"],
    "r\\": ["d"],
    "r-": ["r"],
    "r|": ["u", "d"],
    "r.": ["r"],

    "l/": ["d"],
    "l\\": ["u"],
    "l-": ["l"],
    "l|": ["u", "d"],
    "l.": ["l"],

    "u/": ["r"],
    "u\\": ["l"],
    "u-": ["l", "r"],
    "u|": ["u"],
    "u.": ["u"],

    "d/": ["l"],
    "d\\": ["r"],
    "d-": ["l", "r"],
    "d|": ["d"],
    "d.": ["d"]
}

# @profile
def part1(lines: List[str]):
    grid_l: List[List[str]] = []
    for line in lines:
        grid_l.append(list(line.strip()))
    grid = np.array(grid_l)

    initial_tile = Tile(
        coords=np.array([0, 0]),
        incoming_direction="r"
    )
    current_beams: deque[Beam] = deque([Beam(path=[initial_tile])])

    visited_tiles: Set[Tile] = set([initial_tile])

    iteration = 0
    while current_beams:
        beam = current_beams.popleft()
        last_tile = beam.path[-1]
        effect = grid[tuple(last_tile.coords)]
        
        new_directions = direction_effect_mapping[last_tile.incoming_direction + effect]
        for new_direction in new_directions:
            new_tile_coords = last_tile.coords + direction_to_coord[new_direction]

            if not (0 <= new_tile_coords[0] < grid.shape[0] and 0 <= new_tile_coords[1] < grid.shape[1]):
                continue

            new_tile = Tile(coords=new_tile_coords, incoming_direction=new_direction)
        
            if new_tile in visited_tiles:
                continue

            visited_tiles.add(new_tile)
            new_beam = Beam(path=beam.path.copy())
            new_beam.path.append(new_tile)

            if len(new_beam.path) != len(set(new_beam.path)):
                # Stop condition
                continue

            current_beams.append(new_beam)
    
            # display(grid, new_beam.path)
            if iteration % 1000 == 0:
                print(len(current_beams))
                display(grid, new_beam.path)
        iteration += 1
        # print("\n\n")
    activated_tiles = {v.coords.tobytes().decode(): v for v in visited_tiles}
    return len(activated_tiles)

def display(grid: NDArray[np.str_], visited_tiles: Sequence[Tile]) -> None:
    grid_c: NDArray[np.str_] = copy(grid)
    # print(visited_tiles)
    for tile in visited_tiles:
        grid_c[tuple(tile.coords)] = tile.incoming_direction
    print("\n".join(["".join(row) for row in grid_c]))
        
    

def part2(lines: List[str]):
    return 0


if __name__ == "__main__":
    with open("day16/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))