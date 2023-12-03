from collections import defaultdict
import re


def get_search_coordinates(row_nr, column_nrs):
    """Return a list of row, col coordinates around the given row-columnspan
    
    What I learned here, is that you can have as many yield statements as you like in a generator!
    They will simply be handled one after the other is needed. This means we won't calculate the
    other coordinates if the first yield already contains a special character. Interesting :D"""
    
    # On the row itself, simply look 1 before and 1 after
    yield (row_nr, column_nrs[0] - 1)
    yield (row_nr, column_nrs[1] + 1)

    # On the previous row, start 1 col before all the way to one col after
    for i in range(column_nrs[0] - 1, column_nrs[1] + 2):
        yield (row_nr - 1, i)
    
    for i in range(column_nrs[0] -1, column_nrs[1] + 2):
        yield (row_nr + 1, i)


class Debugger:
    def __init__(self, grid_string, line_width) -> None:
        self.grid_string = grid_string
        self.line_width = line_width - 1

    def add_searched_coord(self, coordinate):
        self.grid_string = self.grid_string[:coordinate] + "#" + self.grid_string[coordinate + 1:]
    
    def debug_print(self):
        for i in range(0, len(self.grid_string), self.line_width):
            print(self.grid_string[i: i + self.line_width])
            # print("\n")


def solution(grid_string: str):
    confirmed_serial_nrs = set()
    gears = defaultdict(list)

    # grid_string = grid_string.replace(".", "a")
    line_width = re.search("\n", grid_string).span()[0]
    grid_string = grid_string.replace("\n", "")

    dbg = Debugger(grid_string, line_width)

    potential_serial_numbers = set(re.finditer(r'\d+', grid_string))
    for match in potential_serial_numbers:
        current_row_nr = match.start() // line_width
        current_column_nrs = (match.start() % line_width, (match.end() - 1) % line_width)

        print(f"====={match}=====")

        for coordinate in get_search_coordinates(current_row_nr, current_column_nrs):
            if coordinate[0] >= 0 and coordinate[1] >= 0 and coordinate[0] * line_width + coordinate[1] < len(grid_string):
                character = grid_string[coordinate[0] * line_width + coordinate[1]]
                dbg.add_searched_coord(coordinate[0] * line_width + coordinate[1])
                if character != "." and not character.isnumeric():
                    # It's a special one!
                    print(f"{match} confirmed! {character}")
                    confirmed_serial_nrs.add(match)
                    # break
                # Part 2
                if character == "*":
                    gears[coordinate].append(int(match.group()))

                
        # dbg.debug_print()
        # print("\n")
    
    non_serial_nrs = [int(m.group()) for m in confirmed_serial_nrs]
    gear_ratios = [v[0] * v[1] for v in gears.values() if len(v) == 2]
    return sum(non_serial_nrs), sum(gear_ratios)


# def part2(grid_string: str)


if __name__ == "__main__":
    with open("day3/input.txt", "r") as f:
        part1, part2 = solution(f.read())
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")

    
    
    