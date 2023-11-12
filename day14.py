from typing import List, TypeAlias, Tuple, Dict, Set, Optional
from utilities import file_handling
import re


Coords: TypeAlias = Tuple[int, int]
Grid: TypeAlias =  Dict[int, Set[int]]

REGEX = r"(\d*),(\d*)"

def in_grid(coord: Coords, current_grid: Grid) -> bool:
    return coord[0] in current_grid and coord[1] in current_grid[coord[0]]


def add_to_grid(coord: Coords, current_grid: Grid) -> Grid:
    if coord[0] in current_grid:
        current_grid[coord[0]].add(coord[1])
    else:
        current_grid[coord[0]] = {coord[1]}



def add_to_grid(coords: Set[Coords], current_grid: Grid) -> Grid:
    if coord[0] in current_grid:
        current_grid[coord[0]].add(coord[1])
    else:
        current_grid[coord[0]] = {coord[1]}

def parse_to_coords(input: str) -> List[Coords]:
    matches = re.findall(REGEX, input)
    result = []
    for match in matches:
        result.append((int(match[0]), int(match[1])))
    return result

def apply_instruction(instruction: List[Coords], current_grid: Grid) -> Grid:
    for i in range(len(instruction)-1):
        this_coord = instruction[i]
        next_coord = instruction[i+1]
        if this_coord[0]==next_coord[0]:
            if this_coord[1] < next_coord[1]:
                range_from = this_coord[1]
                range_to = next_coord[1] + 1
            else:
                range_from = next_coord[1]
                range_to = this_coord[1] + 1
            insert_set = set(range(range_from, range_to))
            if this_coord[0] in current_grid:
                current_grid[this_coord[0]] = current_grid[this_coord[0]].union(insert_set)
            else:
                current_grid[this_coord[0]] = insert_set
        else:
            if this_coord[0] < next_coord[0]:
                range_from = this_coord[0]
                range_to = next_coord[0] + 1
            else:
                range_from = next_coord[0] 
                range_to = this_coord[0] + 1
            for j in range(range_from, range_to):
                if j in current_grid:
                    current_grid[j].add(this_coord[1])
                else:
                    current_grid[j] = {this_coord[1]}
    return current_grid


def drop_sand(position : Coords, current_grid : Grid, max_depth: int, floor_solid: bool) -> Optional[Coords]:
    if in_grid(position, current_grid):
        return None
    
    if position[1] > max_depth and not floor_solid:
        return None

    try_position = (position[0], position[1]+1)
    if (floor_solid and try_position[1] == max_depth) or in_grid(try_position, current_grid):
        try_position = (position[0] - 1, position[1]+1)
        if (floor_solid and try_position[1] == max_depth) or in_grid(try_position, current_grid):
            try_position = (position[0] + 1, position[1]+1)
            if (floor_solid and try_position[1] == max_depth) or in_grid(try_position, current_grid):
                return position
            else:
                return drop_sand(try_position, current_grid, max_depth, floor_solid)
        else:
            return drop_sand(try_position, current_grid, max_depth, floor_solid)
    else:
        return drop_sand(try_position, current_grid, max_depth, floor_solid)



def part1(lines: List[str]) -> int:
    instructions = list(map(parse_to_coords, lines))
    current_grid = {}
    for instruction in instructions:
         current_grid = apply_instruction(instruction, current_grid)    

    max_depth = 0
    for vals in current_grid.values():
        if max(vals) > max_depth:
            max_depth = max(vals)
    sand_count = 0
    position = drop_sand((500,0), current_grid, max_depth, False)
    while position is not None:
        if position[0] in current_grid:
            current_grid[position[0]].add(position[1])
        else:
            current_grid[position[0]] = {position[1]}
        sand_count += 1
        position = drop_sand((500,0), current_grid, max_depth, False)
    return sand_count

def part2(lines: List[str]) -> int:
    instructions = list(map(parse_to_coords, lines))
    current_grid = {}
    for instruction in instructions:
         current_grid = apply_instruction(instruction, current_grid)    

    max_depth = 0
    for vals in current_grid.values():
        if max(vals) > max_depth:
            max_depth = max(vals)
    
    max_depth += 2

    sand_count = 0
    position = drop_sand((500,0), current_grid, max_depth, True)
    while position is not None:
        if position[0] in current_grid:
            current_grid[position[0]].add(position[1])
        else:
            current_grid[position[0]] = {position[1]}
        sand_count += 1
        position = drop_sand((500,0), current_grid, max_depth, True)
    return sand_count


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day14")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
