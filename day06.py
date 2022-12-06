from utilities import file_handling

from utilities.sliding_window import windowstr


def first_unique_group(group_size: int, message: str) -> int:
    windows = windowstr(group_size, message)
    for index, window in enumerate(windows):
        if len(set(window)) == group_size:
            return index + group_size


def part2(line: str) -> int:
    return first_unique_group(14, line)


def part1(line: str) -> int:
    return first_unique_group(4, line)


if __name__ == "__main__":
    data = file_handling.input_as_string("data/day6")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
