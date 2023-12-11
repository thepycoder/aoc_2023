from day11 import part1
from day11 import part2


def test_part1():
    example = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
    assert part1(example.splitlines()) == 374


def test_part1_first_error():
    with open("day11/input.txt") as f:
        assert part1(f.readlines()) > 10571300


def test_part1_full():
    with open("template/input.txt") as f:
        assert part1(f.readlines()) == 0


def test_part2():
    example = """"""
    assert part2(example.splitlines()) == 0


def test_part2_full():
    with open("template/input.txt") as f:
        assert part2(f.readlines()) == 0