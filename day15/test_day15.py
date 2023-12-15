from day15 import part1
from day15 import part2


def test_part1_hash():
    example = """HASH"""
    assert part1(example) == 52


def test_part1():
    example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
    assert part1(example) == 1320


def test_part1_full():
    with open("day15/input.txt") as f:
        assert part1(f.read()) == 504036


def test_part2():
    example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
    assert part2(example) == 145


def test_part2_full():
    with open("template/input.txt") as f:
        assert part2(f.readlines()) == 0