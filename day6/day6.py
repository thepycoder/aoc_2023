from typing import List


def part1(lines: List[str]):
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))

    answer = 1
    for time, distance in zip(times, distances):
        answer *= calc_race(time, distance)
    return answer

def calc_race(time: int, distance: int):
    winning_combinations = 0
    for i in range(time):
        race_distance = i * (time - i)
        if race_distance > distance:
            winning_combinations += 1
    return winning_combinations

def part2(lines: List[str]):
    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))

    return calc_race(time, distance)


if __name__ == '__main__':
    with open("day6/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))