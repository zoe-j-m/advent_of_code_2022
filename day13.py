from typing import List, Tuple, TypeAlias, Set, Union
from enum import Enum
from utilities import file_handling

from functools import cmp_to_key

Item: TypeAlias = Union[int, List]


PASS = -1
FAIL = 1
CONTINUE = 0


def compare(left: Item, right: Item) -> int:
    if not left and right:
        return PASS

    if left and not right:
        return FAIL

    if not left and not right:
        return CONTINUE

    left_copy = left.copy()
    right_copy = right.copy()

    leftItem = left_copy.pop(0)
    rightItem = right_copy.pop(0)
    if type(leftItem) == int and type(rightItem) == int:
        if leftItem > rightItem:
            return FAIL
        elif leftItem < rightItem:
            return PASS
        else:
            return compare(left_copy, right_copy)

    if type(leftItem) == int and type(rightItem) == list:
        result = compare([leftItem], rightItem)
    elif type(leftItem) == list and type(rightItem) == int:
        result = compare(leftItem, [rightItem])
    else:
        result = compare(leftItem, rightItem)

    if result == CONTINUE:
        return compare(left_copy, right_copy)
    else:
        return result


def parse_to_item(input: str) -> Tuple[Item, str]:
    result = []
    while input:
        if input[0] == ",":
            input = input[1:]
        if input[0] == "[":
            parsed_clause, rest = parse_to_item(input[1:])
            result.append([parsed_clause])
            input = rest
        elif input[0] == "]":
            return (result, input[1:])
        else:
            index = 0
            while input[index].isdigit():
                index += 1

            result.append(int(input[0:index]))
            input = input[index:]
    return (result, "")


def part1(lines: List[str]) -> int:
    true_result = 0
    pairs_count = len(lines) // 3
    if len(lines) % 3 == 2:
        pairs_count += 1
    for idx in range(0, pairs_count):
        left_side = parse_to_item(lines[idx * 3])[0]
        print(idx, left_side)
        right_side = parse_to_item(lines[idx * 3 + 1])[0]
        print(idx, right_side)

        if compare(left_side, right_side) != FAIL:
            print("T", idx)
            true_result += idx + 1

    print(left_side)

    return true_result


def p2_compare(left: Item, right: Item) -> int:
    print("Comparing ", left, right)
    if compare(left, right) == FAIL:
        return 1
    else:
        return -1


def part2(lines: List[str]) -> int:
    marker1 = "[[2]]"
    marker2 = "[[6]]"
    lines.append(marker1)
    lines.append(marker2)
    lines = list(filter(lambda x: len(x) > 0, lines))
    items = [item for item, rest in map(parse_to_item, lines)]
    sorts = sorted(items, key=cmp_to_key(p2_compare))

    return (sorts.index(parse_to_item(marker1)[0]) + 1) * (
        sorts.index(parse_to_item(marker2)[0]) + 1
    )


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day13")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
