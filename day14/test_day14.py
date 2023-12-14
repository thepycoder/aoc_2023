from day14 import part1
from day14 import part2


def test_part1():
    example = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
    assert part1(example.splitlines()) == 136


def test_part1_full():
    with open("day14/input.txt") as f:
        assert part1(f.readlines()) == 108935


def test_part2():
    example = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
    assert part2(example.splitlines()) == 64


def test_part2_full():
    with open("template/input.txt") as f:
        assert part2(f.readlines()) == 0