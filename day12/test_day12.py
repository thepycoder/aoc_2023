from day12 import part1
from day12 import part2


def test_part1():
    example = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
    assert part1(example.splitlines()) == 21


def test_part1_simple():
    example = """???.### 1,1,3
"""
    assert part1(example.splitlines()) == 1


def test_part1_simple2():
    example = """?#?#?#?#?#?#?#? 1,3,1,6"""
    assert part1(example.splitlines()) == 1


def test_part1_to_part2():
    example = """.#?.#?.#?.#?.# 1,1,1,1,1"""
    example2 = """.# 1"""
    assert part1(example.splitlines()) == 1
    assert part1(example2.splitlines()) == 1


def test_part1_to_part2_2():
    example = """???.### 1,1,3"""
    example2 = """???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"""
    assert part1(example.splitlines()) == 1
    assert part1(example2.splitlines()) == 1


def test_part1_to_part2_3():
    example = """???.### 1,1,3"""
    example2 = """???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"""
    assert part1(example.splitlines()) == 1
    assert part1(example2.splitlines()) == 1


def test_part1_to_part2_4():
    example = """.#?#???????.????# 1,2,3,2,1"""
    assert part1(example.splitlines()) == 6


# def test_part1_to_part2_5():
#     example = """????.#...#... 4,1,1""".split(" ")
#     example_l = "?".join(example[0]*5) + " " + ",".join([example[1]] * 5)
#     assert part1(example_l.splitlines()) == 16


def test_part1_full():
    with open("day12/input.txt") as f:
        assert part1(f.readlines()) == 7090


def test_part2():
    example = """"""
    assert part2(example.splitlines()) == 0


def test_part2_full():
    with open("template/input.txt") as f:
        assert part2(f.readlines()) == 0