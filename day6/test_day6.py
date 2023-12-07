from day6 import part1, part2


test_input = """Time:      7  15   30
Distance:  9  40  200"""


def test_part1():
    assert part1(test_input.split("\n")) == 288


def test_part1_full():
    with open("day6/input.txt", "r") as f:
        assert part1(f.readlines()) == 5133600


def test_part2():
    assert part2(test_input.split("\n")) == 71503


def test_part2_full():
    with open("day6/input.txt", "r") as f:
        assert part2(f.readlines()) == 40651271