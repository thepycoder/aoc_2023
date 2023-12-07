import re
from typing import List

DIGITS = [
    # "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def part1(lines: List[str]):
    return sum([process_line(line) for line in lines])

def process_line(line: str):
    return int(''.join(map(list(filter(str.isdigit, line)).__getitem__, [0, -1])))

def part2(lines: List[str]):
    result: List[int] = []
    for line in lines:
        matches = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        if matches[0] in DIGITS:
            first_digit = str(DIGITS.index(matches[0]) + 1)
        else:
            first_digit = matches[0]
        
        if matches[-1] in DIGITS:
            last_digit = str(DIGITS.index(matches[-1]) + 1)
        else:
            last_digit = matches[-1]

        # print(first_digit + last_digit)
        result.append(int(first_digit + last_digit))
    return sum(result)


if __name__ == "__main__":
    with open("day1/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))