from typing import List, Tuple, Set
from utilities import file_handling
from functools import reduce

def rucksack_to_pockets(rucksack: str) -> Tuple[Set[str],Set[str]]:
    n = len(rucksack)//2
    return set(rucksack[0:n]), set(rucksack[n:])


def unique_item(rucksack: str) -> str:
    left_pocket, right_pocket = rucksack_to_pockets(rucksack)
    if not left_pocket.intersection(right_pocket):
        print(rucksack, left_pocket, right_pocket)
    return ''.join(left_pocket.intersection(right_pocket))


def group_of_x(rucksacks: List[str], x: int) -> List[List[str]]:
    return zip(*(iter(rucksacks),) * x)

def rucksacks_to_badge(rucksacks: List[str]) -> str:
    items_in_rucksacks = list(map(set, rucksacks))
    shared_items = reduce(lambda x, y: x.intersection(y), items_in_rucksacks)
    return ''.join(shared_items)

a = ord("a")
A = ord("A")

def item_to_priority(item: str) -> int:
    if len(item) == 0:
        return 0
    else:   
        ascii = ord(item[0])
        if ascii >= a:
            return ascii - a + 1
        else:
            return ascii - A + 27


def part2(lines: List[str]) -> int:
    grouped_rucksacks = group_of_x(lines, 3)
    badges = list(map(rucksacks_to_badge, grouped_rucksacks))
    priorities = list(map(item_to_priority, badges))
    return sum(priorities)


def part1(lines: List[str]) -> int:
    unique_items = list(map(unique_item, lines))
    unique_priorities = map(item_to_priority, unique_items)
    return sum(unique_priorities)


if __name__ == '__main__':
    data = file_handling.input_as_lines('data/day3')
    print('Part1: ', part1(data))
    print('Part2: ', part2(data))

