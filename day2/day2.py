import re
import numpy as np
from typing import List, Set

MAX_VALUES = {
    "r": 12,
    "g": 13,
    "b": 14
}


def part1(lines: List[str]):
    impossible: Set[int] = set()
    for line in lines:
        gamestr, cubes = line.split(": ")
        gamenr = int(gamestr.split()[1])

        cube_matches: List[str] = re.findall(r'\d+ [r|g|b]', cubes)
        for match in cube_matches:
            nr, color = match.split()
            if int(nr) > MAX_VALUES[color]:
                impossible.add(gamenr)
                # print(impossible)
    possible = set(range(1, len(lines) + 1)).difference(impossible)
    return sum(possible)

def part2(lines: List[str]):
    total_power = 0
    for line in lines:
        _, cubes = line.split(": ")

        maxes = {
            "r": 0,
            "g": 0,
            "b": 0
        }

        cube_matches: List[str] = re.findall(r'\d+ [r|g|b]', cubes)
        for match in cube_matches:
            nr, color = match.split()
            if int(nr) > maxes[color]:
                maxes[color] = int(nr)
        
        power_of_game = int(np.prod(list(maxes.values())))
        total_power += power_of_game
    return total_power


if __name__ == "__main__":
    with open("day2/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))