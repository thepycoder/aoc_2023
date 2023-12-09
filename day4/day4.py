from collections import defaultdict
from typing import List


def part1(cards: List[str]) -> int:
    points = 0
    for card_line in cards:
        _, card_points = get_points(card_line)
        points += card_points
        # print(f"{card_nr}: {card_points}")
    return points

def get_points(card_line: str, part2: bool = False):
    card_nr, cards = card_line.split(": ")
    winning_str, your_str = cards.split("|")
    winning_nrs = set(map(int, winning_str.strip().split()))
    your_nrs = set(map(int, your_str.strip().split()))
    card_points = len(your_nrs.intersection(winning_nrs))
    if card_points >= 1:
        card_points_list = [1]
        [card_points_list.append(card_points_list[i - 1] * 2) for i in range(1, card_points)]  # type: ignore [func-returns-value]
        return int(card_nr.split()[-1]), card_points_list[-1] if not part2 else len(card_points_list)
    else:
        return int(card_nr.split()[-1]), 0

def part2(cards: List[str]) -> int:
    total_cards = 0
    card_copies: defaultdict[int, int] = defaultdict(int)
    for card_line in cards:
        card_nr, card_points = get_points(card_line, part2=True)
        for _ in range(1 + card_copies[card_nr]):
            total_cards += 1
            for i in range(card_nr + 1, card_nr + 1 + card_points):
                card_copies[i] += 1
    
    return total_cards


if __name__ == "__main__":
    with open("day4/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))