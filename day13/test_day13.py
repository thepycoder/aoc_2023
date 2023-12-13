from day13 import part1
from day13 import part2


def test_part1():
    example = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
    assert part1(example.split("\n\n"))[0] == 405


def test_part1_custom():
    example = """#.##..##.
.##.##.#.
##......#
##......#"""
    assert part1(example.split("\n\n"))[0] == 300


def test_part1_first_error():
    with open("day13/input.txt") as f:
        assert part1(f.read().split("\n\n"))[0] > 31822


def test_part1_full():
    with open("day13/input.txt") as f:
        assert part1(f.read().split("\n\n"))[0] == 31956


def test_part2():
    example = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
    answer_map = part1(example.split("\n\n"))[1]
    assert part2(example.split("\n\n"), answer_map) == 400


def test_part2_first_error():
    with open("day13/input.txt") as f:
        content = f.read().split("\n\n")
        answer_map = part1(content)[1]
        assert part2(content, answer_map) < 48487


def test_part2_full():
    with open("day13/input.txt") as f:
        content = f.read().split("\n\n")
        answer_map = part1(content)[1]
        assert part2(content, answer_map) == 37617