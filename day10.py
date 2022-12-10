from typing import List, Tuple

from utilities import file_handling

def check_output(clock: int, reg_x: int, output: int) -> int:
    if abs(reg_x - ((clock - 1) % 40)) > 1:
        pixel = '.'
    else:
        pixel = '#'

    if clock % 40 == 0:
        print(pixel)
    else:
        print(pixel, end = '')
        
    if (clock - 20) % 40 == 0:
        return output + clock * reg_x 
    else:
        return output

def execute(clock: int, reg_x: int, instruction: Tuple[str,int], output: int) -> Tuple[int, int, int]:
    command, value = instruction
    if command == 'noop':
        clock += 1
        output = check_output(clock, reg_x, output)
    elif command == 'addx':
        clock += 1
        output = check_output(clock, reg_x, output)
        clock += 1
        output = check_output(clock, reg_x, output)
        reg_x += value
    else:
        output = check_output(clock, reg_x, output)
    
    return clock, reg_x, output



def parse_line(line : str) -> Tuple[str, int]:
    command = line[0:4]
    if command != 'noop':
        value = int(line[5:])
    else:
        value = 0
    return command, value


def part1(lines: List[str]) -> int:
    instructions = list(map(parse_line, lines))
    clock = 0
    reg_x = 1
    output = 0
    for instruction in instructions:
        clock, reg_x, output = execute(clock, reg_x, instruction, output)
    return output


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day10")
    print("Part1: ", part1(data))
  