from day7 import part1
from day7 import part2


def test_part1():
    test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    assert part1(test_input.split("\n")) == 6440


def test_part1_first_error():
    with open("day7/input.txt", "r") as f:
        assert part1(f.readlines()) > 247581863


def test_part1_full():
    with open("day7/input.txt", "r") as f:
        assert part1(f.readlines()) == 248113761


def test_part2():
    test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    assert part2(test_input.split("\n")) == 5905


def test_part2_first_error():
    with open("day7/input.txt", "r") as f:
        assert part2(f.readlines()) < 247179935


def test_part2_full():
    with open("day7/input.txt", "r") as f:
        assert part2(f.readlines()) == 246285222