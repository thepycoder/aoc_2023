from day10 import part1
from day10 import part2


def test_part1():
    example = """.....
.S-7.
.|.|.
.L-J.
....."""
    assert part1(example.splitlines())[1] == 4


def test_part1_b():
    example = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""
    assert part1(example.splitlines())[1] == 4


def test_part1_c():
    example = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""
    assert part1(example.splitlines())[1] == 8


def test_part1_full():
    with open("day10/input.txt") as f:
        assert part1(f.readlines())[1] == 6838


def test_part2():
    example = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
    assert part2(example.splitlines(), set(part1(example.splitlines())[0])) == 4


def test_part2_b():
    example = """..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
.........."""
    assert part2(example.splitlines(), set(part1(example.splitlines())[0])) == 4


def test_part2_c():
    example = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
    assert part2(example.splitlines(), set(part1(example.splitlines())[0])) == 8


def test_part2_d():
    example = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
    assert part2(example.splitlines(), set(part1(example.splitlines())[0])) == 10


def test_part2_full():
    with open("day10/input.txt", "r") as f:
        content = f.readlines()
        loop, distance = part1(content)
        print(distance)
        assert part2(content, set(loop)) == 451