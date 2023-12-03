from day3 import solution
# from day3 import part2

def test_part1():
    test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    assert solution(test_input)[0] == 4361


def test_part1_2():
    test_input = """...
123
$.."""
    assert solution(test_input)[0] == 123

def test_part2():
    test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    assert solution(test_input)[1] == 467835