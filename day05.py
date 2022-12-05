from typing import List, Dict
from utilities import file_handling
import re

MOVE_REGEX = r"move (\d*) from (\d*) to (\d*)"


def parse_to_moves(lines: List[str]) -> List[Dict[str, int]]:
    result = []
    for line in lines:
        capture_groups = re.search(MOVE_REGEX, line).groups()
        capture_values = list(map(int, capture_groups))
        result.append({
            'move': capture_values[0],
            'from': capture_values[1],
            'to': capture_values[2]
        })
    return result


def parse_to_position(lines: List[str]) -> Dict[int, List[str]]:
    guide = lines[-1][::-1].strip()
    lines = lines[:-1]
    max_pile = int(guide[0])

    result = {}
    for line in lines:
        print(line)
        for pile in range(1, max_pile + 1):
            position = (pile - 1) * 4 + 1
            if position < len(line) and line[position] != ' ':
                if pile in result:
                    result[pile].append(line[position])
                else:
                    result[pile] = [line[position]]

    return result


def apply_move(position: Dict[int, List[str]], move: Dict[str, int], reverse: bool):
    no_to_move = move['move']
    crates_at_from = position[move['from']]
    crates_to_move = crates_at_from[0:no_to_move]
    if reverse:
        crates_to_move.reverse()
    new_at_from = crates_at_from[no_to_move:]
    new_at_to = crates_to_move + position[move['to']]
    position[move['from']] = new_at_from
    position[move['to']] = new_at_to


def process(lines: List[str], reverse: bool) -> str:
    starting_position_lines = []
    line_index = 0
    while lines[line_index] != "":
        starting_position_lines.append(lines[line_index])
        line_index += 1

    lines = lines[line_index+1:]

    position = parse_to_position(starting_position_lines)
    moves = parse_to_moves(lines)

    for move in moves:
        apply_move(position, move, reverse)

    piles = list(position.keys())
    piles.sort()
    return ''.join(position[pile][0] for pile in piles if len(position[pile]))


def part2(lines: List[str]) -> str:
    return process(lines, False)


def part1(lines: List[str]) -> str:
    return process(lines, True)


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day5")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
