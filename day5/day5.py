from dataclasses import dataclass, field
from multiprocessing import Pool
from typing import Any, List, Tuple

from tqdm import tqdm


@dataclass
class Range:
    destination_range_start: int
    source_range_start: int
    range_length: int


@dataclass
class AlmanacSection:
    ranges: List[Range] = field(default_factory=list)

    def map_seed_nr(self, seed_nr: int):
        for rnge in self.ranges:
            if rnge.source_range_start <= seed_nr <= rnge.source_range_start + rnge.range_length:
                return rnge.destination_range_start + (seed_nr - rnge.source_range_start)
        return seed_nr


@dataclass
class Almanac:
    sections: List[AlmanacSection] = field(default_factory=list)

    def map_seed_nr(self, seed_nr: int) -> List[int]:
        current_seed_nr = seed_nr
        seed_mapping: List[int] = [current_seed_nr]
        for section in self.sections:
            current_seed_nr = section.map_seed_nr(current_seed_nr)
            seed_mapping.append(current_seed_nr)
        return seed_mapping
    

def read_almanac(alamanac_sections_str: List[str]):
    almanac = Almanac()
    for section in alamanac_sections_str[1:]:
        almanac_section = AlmanacSection()
        for rnge in section.strip().split("\n")[1:]:
            r = Range(*list(map(int, rnge.split())))
            almanac_section.ranges.append(r)
        almanac.sections.append(almanac_section)
    return almanac


def part1(almanac_str: str):
    alamanac_sections_str = almanac_str.split("\n\n")
    seeds: List[int] = list(map(int, alamanac_sections_str[0].split(": ")[1].split()))
    
    almanac: Almanac = read_almanac(alamanac_sections_str)
    
    min_location: float = float('inf')
    for seed in seeds:
        seed_mapping = almanac.map_seed_nr(seed)
        print(f"{seed_mapping[0]}: {seed_mapping[-1]}\n{seed_mapping}")
        if seed_mapping[-1] < min_location:
            min_location = seed_mapping[-1]

    return min_location


def part2(almanac_str: str):
    alamanac_sections_str = almanac_str.split("\n\n")
    seed_ranges: List[int] = list(map(int, alamanac_sections_str[0].split(": ")[1].split()))

    almanac: Almanac = read_almanac(alamanac_sections_str)

    arguments: List[Tuple[Almanac, int, int]] = []
    for seed_index in range(0, len(seed_ranges), 2):
        start_seed_range = seed_ranges[seed_index]
        length_seed_range = seed_ranges[seed_index + 1]
        arguments.append((almanac, start_seed_range, length_seed_range))
    with Pool() as p:
        results = p.starmap(calc_seed_range, arguments)
        print(results)
    return min(results)
    

def calc_seed_range(almanac: Almanac, start_seed_range: int, length_seed_range: int) -> float:
    min_location: float = float('inf')
    for i in tqdm(range(length_seed_range)):
        seed_mapping = almanac.map_seed_nr(start_seed_range + i)
            # print(f"{seed_mapping[0]}: {seed_mapping[-1]}\n{seed_mapping}")
        if seed_mapping[-1] < min_location:
            min_location = seed_mapping[-1]
    return min_location




if __name__ == "__main__":
    with open("day5/input.txt", "r") as f:
        content = f.read()
        print(part1(content))
        print(part2(content))
