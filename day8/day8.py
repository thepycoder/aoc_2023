import numpy as np
from typing import Dict, List, Tuple


def part1(lines: List[str]) -> int:
    node_mapping: Dict[str, Tuple[str, str]] = dict()

    instructions = list(lines[0].strip())

    for line in lines[2:]:
        parent, children = line.strip().split(" = ")
        both_children = children.split(", ")
        node_mapping[parent] = (both_children[0][1:], both_children[1][:-1])
    
    current_node = "AAA"
    instruction_pointer = 0
    while current_node != "ZZZ":
        instruction = instructions[instruction_pointer % len(instructions)]
        if instruction == "L":
            current_node = node_mapping[current_node][0]
        else:
            current_node = node_mapping[current_node][1]
        instruction_pointer += 1
    return instruction_pointer


def part2(lines: List[str]):
    node_mapping: Dict[str, Tuple[str, str]] = dict()
    instructions = list(lines[0].strip())
    current_nodes: List[str] = []

    for line in lines[2:]:
        parent, children = line.strip().split(" = ")
        both_children = children.split(", ")
        node_mapping[parent] = (both_children[0][1:], both_children[1][:-1])
        if parent.endswith("A"):
            current_nodes.append(parent)
    

    cycle_length: List[List[int]] = []
    for _ in current_nodes:
        cycle_length.append([])

    instruction_pointer = 0
    while not all(truth_check := [c.endswith("Z") for c in current_nodes]):
        for i, t in enumerate(truth_check):
            if t:
                cycle_length[i].append(instruction_pointer)
        if all(cycle_length):
            # At this point we know the regular cycle interval of each of the nodes
            # so all we have to do is find the lcm of all of them!
            lcm = np.lcm.reduce([c[0] for c in cycle_length])
            # Okay, this is seriously cool!
            return lcm
        instruction = instructions[instruction_pointer % len(instructions)]
        if instruction == "L":
            for i in range(len(current_nodes)):
                current_nodes[i] = node_mapping[current_nodes[i]][0]
        else:
            for i in range(len(current_nodes)):
                current_nodes[i] = node_mapping[current_nodes[i]][1]
        instruction_pointer += 1
    return instruction_pointer


if __name__ == "__main__":
    with open("day8/input.txt", "r") as f:
        content = f.readlines()
        print(part1(content))
        print(part2(content))

