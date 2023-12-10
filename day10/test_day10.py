from day10 import part1
from day10 import part2


def test_part1():
    example = """.....
.S-7.
.|.|.
.L-J.
....."""
    assert part1(example.splitlines()) == 4


def test_part1_b():
    example = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""
    assert part1(example.splitlines()) == 4


def test_part1_full():
    with open("template/input.txt") as f:
        assert part1(f.readlines()) == 0


def test_part2():
    example = """"""
    assert part2(example.splitlines()) == 0


def test_part2_full():
    with open("template/input.txt") as f:
        assert part2(f.readlines()) == 0