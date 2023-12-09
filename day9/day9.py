from typing import List, Callable
import numpy as np
from numpy.typing import NDArray


def process_line(line: str, calculate_total: Callable[[List[NDArray[np.int32]]], int]) -> int:
    history: List[NDArray[np.int32]] = [np.array([int(value) for value in line.split()])]
    while np.sum(history[-1]) != 0:
        history.append(np.diff(history[-1]))

    return calculate_total(history)

def calculate_total_part1(history: List[NDArray[np.int32]]) -> int:
    line_total = 0
    for sequence in history[::-1]:  # Reverse the list of diff sequences
        line_total += sequence[-1]
    return line_total

def calculate_total_part2(history: List[NDArray[np.int32]]) -> int:
    line_total = 0
    for sequence in history[::-1]:  # Reverse the list of diff sequences
        line_total = -1 * (line_total - sequence[0])
    return line_total

def part1(lines: List[str]) -> int:
    total_sum = 0
    for line in lines:
        line_total = process_line(line, calculate_total_part1)
        print(f"Line total: {line_total}")
        total_sum += line_total
    return total_sum

def part2(lines: List[str]) -> int:
    total_sum = 0
    for line in lines:
        line_total = process_line(line, calculate_total_part2)
        print(f"Line total: {line_total}")
        total_sum += line_total
    return total_sum


if __name__ == "__main__":
    with open("day9/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))