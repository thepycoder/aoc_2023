from day8 import part1
from day8 import part2


def test_part1():
    test_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
    assert part1(test_input.split("\n")) == 2

def test_part1_b():
    test_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
    assert part1(test_input.split("\n")) == 6

def test_part1_first_error():
    with open("day8/input.txt", "r") as f:
        content = f.readlines()
        assert part1(content) > 13621


def test_part1_first_full():
    with open("day8/input.txt", "r") as f:
        content = f.readlines()
        assert part1(content) == 14681


def test_part2_first_full():
    with open("day8/input.txt", "r") as f:
        content = f.readlines()
        assert part2(content) == 14321394058031


def test_part2():
    test_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    assert part2(test_input.split("\n")) == 6

