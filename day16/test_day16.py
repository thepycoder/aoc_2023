from day16 import part1
from day16 import part2


def test_part1():
    example = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
    assert part1(example.splitlines()) == 46


def test_part1_full():
    with open("day16/input.txt") as f:
        assert part1(f.readlines()) == 7482


def test_part2():
    example = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
    assert part2(example.splitlines()) == 51


def test_part2_full():
    with open("day16/input.txt") as f:
        assert part2(f.readlines()) == 0