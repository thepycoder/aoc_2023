from __future__ import annotations
from collections import defaultdict, deque
from dataclasses import dataclass
import re


@dataclass
class Lens:
    label: str
    focal_length: int = -1
    
    def __eq__(self, __value: object) -> bool:
        return self.label == __value.label

    def __repr__(self) -> str:
        return f"[{self.label} {self.focal_length}]"


def part1(line: str):
    line = line.replace("\n", "")
    total = 0
    for instruction in line.split(","):
        total += calc_hash(instruction)
    return total

def calc_hash(instruction: str):
    current_value = 0
    for char in list(instruction):
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    print(f"{instruction}: {current_value}")
    return current_value

def part2(line: str):
    line = line.replace("\n", "")
    boxes: defaultdict[int, deque[Lens]] = defaultdict(deque)
    for instruction in line.split(","):
        instr = re.search(r"([a-z]*)([-|=])(\d?)", instruction)
        if not instr:
            raise ValueError(f"Something went wrong! Can't extract the label for {instruction}")
        label = instr.groups()[0]
        box_nr = calc_hash(label)
        operation = instr.groups()[1]

        if operation == "-":
            try:
                boxes[box_nr].remove(Lens(label))
            except ValueError:
                pass

        if operation == "=":
            focal_length = int(instr.groups()[2])
            new_lens = Lens(label, focal_length)
            box = boxes[box_nr]
            dup = False
            for i, lens in enumerate(box):
                if lens.label == new_lens.label:
                    dup = True
                    break
            if dup:
                box.remove(lens)
                box.insert(i, new_lens)
            else:
                box.append(new_lens)
        
        print(f"After {instruction}")
        for box_nr, contents in boxes.items():
            print(f"Box {box_nr}: {contents}")

    total = 0
    for box_nr, box in boxes.items():
        for lens_slot, lens in enumerate(box):
            total += (1 + box_nr) * (lens_slot + 1) * lens.focal_length

    return total


if __name__ == "__main__":
    with open("day15/input.txt", "r") as f:
        content = f.read()
        print(part1(content))
        print(part2(content))