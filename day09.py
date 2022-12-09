from typing import List, Tuple, Set, Dict

from utilities import file_handling

from utilities.matrices import Matrix

from functools import reduce


def line_to_move(line: str) -> Tuple[str, int]:
    return line[0], int(line[2:])


def apply_move_to_head(direction: str, head: Tuple[int, int]) -> Tuple[int, int]:
    x, y = head
    if direction == "D":
        head = x, y - 1
    elif direction == "U":
        head = x, y + 1
    elif direction == "L":
        head = x - 1, y
    else:
        head = x + 1, y

    return head


def distance_between(head: Tuple[int, int], tail: Tuple[int, int]) -> int:
    head_x, head_y = head
    tail_x, tail_y = tail
    x_diff = abs(head_x - tail_x)
    y_diff = abs(head_y - tail_y)
    return max(x_diff, y_diff)


def move_tail(head: Tuple[int, int], tail: Tuple[int, int]) -> Tuple[int, int]:
    head_x, head_y = head
    tail_x, tail_y = tail
    if abs(head_x - tail_x) and abs(head_y - tail_y):
        tail_x += (head_x - tail_x) // abs(head_x - tail_x)
        tail_y += (head_y - tail_y) // abs(head_y - tail_y)
    elif abs(head_x - tail_x) > 1:
        tail_x += (head_x - tail_x) // abs(head_x - tail_x)
    elif abs(head_y - tail_y) > 1:
        tail_y += (head_y - tail_y) // abs(head_y - tail_y)

    return tail_x, tail_y


def part2(lines: List[str]) -> int:
    moves = map(line_to_move, lines)
    tails = []
    for i in range(10):
        tails.append((0, 0))
    visited = set((0, 0))
    for move in moves:
        direction, distance = move
        for idx in range(distance):
            tails[0] = apply_move_to_head(direction, tails[0])
            for index in range(0, len(tails) - 1):
                first = tails[index]
                second = tails[index + 1]
                if distance_between(first, second) > 1:
                    second = move_tail(first, second)
                    if index == len(tails) - 2:
                        visited.add(second)
                tails[index + 1] = second

    return len(visited)


def part1(lines: List[str]) -> int:
    moves = map(line_to_move, lines)
    head = 0, 0
    tail = 0, 0
    visited = set(tail)
    for move in moves:
        direction, distance = move
        for idx in range(distance):
            head = apply_move_to_head(direction, head)

            if distance_between(head, tail) > 1:
                tail = move_tail(head, tail)
                visited.add(tail)

    return len(visited)


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day9")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
