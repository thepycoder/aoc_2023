from day1 import part1
from day1 import part2


def test_part1():
    example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert part1(example.splitlines()) == 142


def test_part2():
    example = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert part2(example.splitlines()) == 281