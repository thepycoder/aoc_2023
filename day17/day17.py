import dis
from math import cos, dist
import numpy as np
from typing import List, Optional, Tuple, Dict
from heapq import heappush, heappop

def get_neighbors(position: Tuple[int, int], last_direction: Tuple[int, int], consecutive_steps: int, max_rows: int, max_cols: int) -> List[Tuple[Tuple[int, int], Tuple[int, int], int]]:
    """
    Get all possible neighbors from the current position considering the constraints.
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    neighbors = []
    for d in directions:
        new_pos = (position[0] + d[0], position[1] + d[1])
        if 0 <= new_pos[0] < max_rows and 0 <= new_pos[1] < max_cols:
            if d == last_direction:
                if consecutive_steps < 3:
                    neighbors.append((new_pos, d, consecutive_steps + 1))
            else:
                neighbors.append((new_pos, d, 1))
    return neighbors

def dijkstra(cost_map: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[int, Dict[Tuple[float, int], Optional[Tuple[int, int]]]]:
    """
    Perform Dijkstra's algorithm considering the given constraints.
    """
    rows, cols = cost_map.shape
    dist = {(r, c): float('inf') for r in range(rows) for c in range(cols)}
    dist[start] = 0
    predecessors: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}

    # The heap queue will store tuples of the form (cost, current_position, last_direction, consecutive_steps)
    pq = [(0, start, (0, 0), 0)]  # Initial direction and consecutive steps are set to 0
    
    while pq:
        current_dist, current_position, last_direction, consecutive_steps = heappop(pq)
        if current_position == end:
            return current_dist, predecessors

        for neighbor, direction, steps in get_neighbors(current_position, last_direction, consecutive_steps, rows, cols):
            new_dist = current_dist + cost_map[neighbor]
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                predecessors[neighbor] = current_position
                heappush(pq, (new_dist, neighbor, direction, steps))
    
    return float('inf'), predecessors  # If no path found


def trace_path(predecessors: Dict[Tuple[int, int], Tuple[int, int]], end: Tuple[int, int], cost_map: np.ndarray) -> np.ndarray:
    """
    Trace the path from the end node to the start node and mark it on the map.
    """
    path_map = np.copy(cost_map)
    current = end
    while current:
        path_map[current] = 0  # Marking the path with 0
        current = predecessors[current]
    return path_map


def part1(lines: List[str]):
    grid_l: List[List[int]] = []
    for line in lines:
        grid_l.append(list(map(int, list(line.strip()))))
    grid = np.array(grid_l)

    start = (0, 0)
    end = (grid.shape[0] - 1, grid.shape[1] - 1)
    distance, predecessors = dijkstra(grid, start, end)
    print(trace_path(predecessors=predecessors, end=end, cost_map=grid))
    return distance

def part2(lines: List[str]):
    return 0

# # Example usage
# cost_map = np.array([[1, 1, 1],
#                      [10, 100, 10],
#                      [1, 1, 1]])
# start = (0, 0)
# end = (2, 2)

# print(dijkstra(cost_map, start, end))
