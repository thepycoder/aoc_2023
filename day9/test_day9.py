from day9 import part1
from day9 import part2


def test_part1():
    example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
    assert part1(example.splitlines()) == 114


def test_part1_custom():
    example = """-1 -3 -5 -7"""
    assert part1(example.splitlines()) == -9


def test_part1_first_error():
    with open("day9/input.txt") as f:
        assert part1(f.readlines()) < 1800830724


def test_part1_full():
    with open("day9/input.txt") as f:
        assert part1(f.readlines()) == 1798691765


def test_part2():
    example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
    assert part2(example.splitlines()) == 2


def test_part2_full():
    with open("day9/input.txt") as f:
        assert part2(f.readlines()) == 1104