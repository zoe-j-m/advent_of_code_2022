from typing import List, Tuple, Set
from utilities import file_handling
import re

REGEX = r"(\d*)-(\d*),(\d*)-(\d*)"


def input_to_assignments(line: str) -> Tuple[Set[int], Set[int]]:
    capture_groups = re.search(REGEX, line).groups()
    capture_values = list(map(int, capture_groups))
    return set(range(capture_values[0], capture_values[1] + 1)), set(
        range(capture_values[2], capture_values[3] + 1)
    )


def assignments_overlap(assignment1: Set[int], assignment2: Set[int]) -> bool:
    return assignment1.issubset(assignment2) or assignment2.issubset(assignment1)


def assignments_intersect(assignment1: Set[int], assignment2: Set[int]) -> bool:
    return len(assignment1.intersection(assignment2)) != 0


def part2(lines: List[str]) -> int:
    assignments = list(map(input_to_assignments, lines))
    return sum(
        assignments_intersect(assignment1, assignment2)
        for assignment1, assignment2 in assignments
    )


def part1(lines: List[str]) -> int:
    assignments = list(map(input_to_assignments, lines))
    return sum(
        assignments_overlap(assignment1, assignment2)
        for assignment1, assignment2 in assignments
    )


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day4")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
