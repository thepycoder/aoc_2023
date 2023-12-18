from collections import deque
from dataclasses import dataclass
from typing import List, Set, Tuple

import numpy as np


@dataclass
class Node:
    coords: Tuple[int, int]
    color: str


def print_grid(nodes: List[Node]):
    """ChatGPT generated: Write a function that takes an arbitrary list of Nodes (like `nodes`) and prints a 2D grid, where each point inside `nodes` is presented as `#` and each point that is not by `.` (+context from code)"""
    # Find the minimum and maximum coordinates to determine the grid size
    min_x = min(node.coords[0] for node in nodes)
    min_y = min(node.coords[1] for node in nodes)
    max_x = max(node.coords[0] for node in nodes)
    max_y = max(node.coords[1] for node in nodes)

    # Calculate the grid size
    grid_width = max_x - min_x + 1
    grid_height = max_y - min_y + 1

    # Create an empty grid filled with '.'
    grid = [['.' for _ in range(grid_height)] for _ in range(grid_width)]

    # Mark the nodes on the grid with '#'
    for node in nodes:
        x, y = node.coords
        grid[x - min_x][y - min_y] = '#'

    # Print the grid
    for row in grid:
        print(' '.join(row))
    
    print("\n\n")


def flood_fill(starting_coord: Tuple[int, int], boundary: Set[Tuple[int, int]]):
    filled_coords: Set[Tuple[int, int]] = set()
    to_check: deque[Tuple[int, int]] = deque([starting_coord])

    while to_check:
        coord = to_check.popleft()
        if coord in boundary or coord in filled_coords:
            continue
        to_check.append((coord[0] + 1, coord[1]))
        to_check.append((coord[0] - 1, coord[1]))
        to_check.append((coord[0], coord[1] + 1))
        to_check.append((coord[0], coord[1] - 1))
        filled_coords.add(coord)
    
    return filled_coords

def part1(lines: List[str]):
    nodes: List[Node] = [Node(coords=(0, 0), color="#ffffff")]
    for line in lines:
        current_location = nodes[-1].coords
        direction, amount_s, color_s = line.strip().split(" ")
        amount = int(amount_s)
        color = color_s.replace("(", "").replace(")", "")

        if direction == "U":
            for i in range(1, amount + 1):
                nodes.append(Node(coords=(current_location[0] - i, current_location[1]), color=color))
        elif direction == "D":
            for i in range(1, amount + 1):
                nodes.append(Node(coords=(current_location[0] + i, current_location[1]), color=color))
        elif direction == "L":
            for i in range(1, amount + 1):
                nodes.append(Node(coords=(current_location[0], current_location[1] - i), color=color))
        elif direction == "R":
            for i in range(1, amount + 1):
                nodes.append(Node(coords=(current_location[0], current_location[1] + i), color=color))
        
    print_grid(nodes)

    # Find a row where there are no consecutive "#", so we can use the raycasting algo to find a point def inside the loop
    # Then floodfill from there
    min_r = min(node.coords[0] for node in nodes)
    max_r = max(node.coords[0] for node in nodes)
    max_c = max(node.coords[1] for node in nodes)
    trench = set(n.coords for n in nodes)
    for r in range(min_r, max_r):
        consecutive_trenchnodes = any(np.diff([n.coords[1] for n in nodes if n.coords[0] == r]) == 1)
        if not consecutive_trenchnodes:
            for c in range(max_c + 1):
                if (r, c) in trench:
                    continue
                # If not part of the trench, raycast to check if it is inside trench boundaries
                trench_hits = len(set((r, c - i) for i in range(1, c + 1)).intersection(trench))

                if trench_hits % 2 != 0:
                    # We're inside and should start floodfilling from here!
                    filled_coords = flood_fill((r, c), trench)
                    return len(filled_coords) + len(nodes) - 1 # Get rid of the starting node

    print_grid(nodes)


def part2(lines: List[str]):
    return 0


if __name__ == "__main__":
    with open("day18/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))