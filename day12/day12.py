from collections import defaultdict, deque
from dataclasses import dataclass, replace
from typing import List


@dataclass
class HotSpringLine:
    line_nr: int
    hotsprings: str
    checksum: List[int]


def check_line_is_valid(hotspringline: HotSpringLine):
    # Replace all . and ? and check if no chunk is already too large
    # chunks = hotspringline.hotsprings.replace(".", " ").split()
    # index = 0
    # for chunk in chunks:
    #     if chunk.count("#") == len(chunk):
    #         if index > len(hotspringline.checksum) - 1:
    #             return False
    #         if len(chunk) > hotspringline.checksum[index]:
    #             return False
    #         index += 1
    # If we have more contiguous groups than we need: invalid
    # if len(chunks) > len(hotspringline.checksum):
    #     return False

    # If the amount of ? is smaller than the remaining space needed
    if hotspringline.hotsprings.count("#") + hotspringline.hotsprings.count("?") < sum(
        hotspringline.checksum
    ):
        return False

    # Final check
    if hotspringline.hotsprings.count("?") == 0:
        chunks = hotspringline.hotsprings.replace(".", " ").replace("?", " ").split()
        if len(chunks) != len(hotspringline.checksum):
            return False
        for i, chunk in enumerate(chunks):
            if len(chunk) > hotspringline.checksum[i]:
                return False

    return True


def part1(lines: List[str]):
    queue: deque[HotSpringLine] = deque()
    for i, line in enumerate(lines):
        parts = line.strip().split()
        hotspringline = HotSpringLine(i, parts[0], list(map(int, parts[1].split(","))))
        queue.append(hotspringline)

    running_total: defaultdict[int, int] = defaultdict(int)
    while len(queue) > 0:
        hotspringline = queue.popleft()

        # If complete and valid: add to our running total
        if hotspringline.hotsprings.count("?") == 0:
            running_total[hotspringline.line_nr] += 1
            continue

        # If not complete yet, create 2 variations: one with the next ? filled by a . and one with a ?
        # then check their validity and if true, add the new line to the queue
        dot = replace(hotspringline)
        dot.hotsprings = dot.hotsprings.replace(
            "?", ".", 1
        )  # 1 means only replace first occurence
        if check_line_is_valid(dot):
            queue.append(dot)

        hashtag = replace(hotspringline)
        hashtag.hotsprings = hashtag.hotsprings.replace("?", "#", 1)
        if check_line_is_valid(hashtag):
            queue.append(hashtag)

        print(len(queue))
    print(running_total)
    return sum(running_total.values())


def part2(lines: List[str]):
    return 0


if __name__ == "__main__":
    with open("day12/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))
