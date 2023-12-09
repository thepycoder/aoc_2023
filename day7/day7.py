from __future__ import annotations
from collections import Counter
from typing import List


card_mapping = {
    "A": 14,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
}

class Hand:
    def __init__(self, hand: List[int], bid: int, type: int) -> None:
        self.hand = hand
        self.bid = bid
        self.type = type
    
    @staticmethod
    def from_strings(s_hand: str, s_bid: str, part2: bool = False) -> Hand:
        hand = [card_mapping[char] if not char.isdigit() else int(char) for char in list(s_hand)]
        bid = int(s_bid)

        # Reset the value of the Joker for part 2
        if part2:
            hand = [1 if x == 11 else x for x in hand]

        # This will count occurences into a dict, sorted by most occuring first!
        card_counts = Counter(hand)

        # In part2: consider the J to be the same as the highest other card
        jokers = card_counts.get(1, None)
        if jokers and jokers < 5:
            # Remove the jokers from the counter
            del card_counts[1]
            # Add the amount of jokers to the most occuring AND highest card in order to make as high a hand as possible
            card_to_add_jokers_to = sorted(card_counts.most_common(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]
            card_counts[card_to_add_jokers_to] += jokers


        values = [c[1] for c in card_counts.most_common()]

        if len(card_counts) == 1:
            type = 6  # Five of a kind
        elif list(values) == [4, 1]:
            type = 5  # Four of a kind
        elif list(values) == [3, 2]:
            type = 4  # Full house
        elif list(values) == [3, 1, 1]:
            type = 3  # Three of a kind
        elif list(values) == [2, 2, 1]:
            type = 2  # Two pair
        elif list(values) == [2, 1, 1, 1]:
            type = 1  # One pair
        else:
            type = 0  # High card

        return Hand(hand=hand, bid=bid, type=type)
    

    def __lt__(self, other: Hand):
        if self.type != other.type:
            # If the type is different, it's easy to compare
            return self.type < other.type
        else:
            for s, o in zip(self.hand, other.hand):
                if s != o:
                    return s < o
    
    def __repr__(self) -> str:
        return f"{self.type}: {self.hand} -> {self.bid}"


def part1(lines: List[str]) -> int:
    hands: List[Hand] = []
    for line in lines:
        s_hand, s_bid = line.split()
        hands.append(Hand.from_strings(s_hand=s_hand, s_bid=s_bid))
    
    total: int = 0
    for i, hand in enumerate(sorted(hands)):
        total += (i + 1) * hand.bid
    
    return total


def part2(lines: List[str]) -> int:
    hands: List[Hand] = []
    for line in lines:
        s_hand, s_bid = line.split()
        hands.append(Hand.from_strings(s_hand=s_hand, s_bid=s_bid, part2=True))
    
    total: int = 0
    for i, hand in enumerate(sorted(hands)):
        total += (i + 1) * hand.bid
    
    return total


if __name__ == "__main__":
    with open("day7/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))
