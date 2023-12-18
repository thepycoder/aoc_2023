from day17 import part1
from day17 import part2


def test_part1():
    example = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
    assert part1(example.splitlines()) == 102


def test_part1_full():
    with open("template/input.txt") as f:
        assert part1(f.readlines()) == 0


def test_part2():
    example = """"""
    assert part2(example.splitlines()) == 0


def test_part2_full():
    with open("template/input.txt") as f:
        assert part2(f.readlines()) == 0