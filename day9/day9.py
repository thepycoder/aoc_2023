from typing import List
import numpy as np
from numpy.typing import NDArray


def part1(lines: List[str]):
    total_sum = 0
    for line in lines:
        history: List[NDArray[np.int32]] = [np.array([int(value) for value in line.split()])]
        while np.sum(history[-1]) != 0:
            history.append(np.diff(history[-1]))
        
        line_total = 0
        for sequence in history[::-1]:  # Reverse the list of diff sequences
            line_total += sequence[-1]
        
        print(f"Line total: {line_total}")
        total_sum += line_total
    return total_sum

def part2(lines: List[str]):
    total_sum = 0
    for line in lines:
        history: List[NDArray[np.int32]] = [np.array([int(value) for value in line.split()])]
        while np.sum(history[-1]) != 0:
            history.append(np.diff(history[-1]))
        
        line_total = 0
        for sequence in history[::-1]:  # Reverse the list of diff sequences
            line_total = -1 * (line_total - sequence[0])
        
        print(f"Line total: {line_total}")
        total_sum += line_total
    return total_sum


if __name__ == "__main__":
    with open("day9/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))