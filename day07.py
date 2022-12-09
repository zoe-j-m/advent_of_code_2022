import re
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

from utilities import file_handling


class SystemItem(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass


class Directory(SystemItem):
    def __init__(
        self, name: str, items: List[SystemItem], parent: Optional["Directory"]
    ):
        self.name = name
        self.items = items
        self.parent = parent

    def get_size(self) -> int:
        return sum(item.get_size() for item in self.items)


class File(SystemItem):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size


def parse_command(command: str, current_directory: Directory) -> Directory:
    if command == "cd ..":
        return current_directory.parent
    elif command == "ls":
        return current_directory
    elif command.startswith("cd"):
        new_directory = command[3:]
        item: Directory = next(
            item
            for item in current_directory.items
            if item.name == new_directory and item.__class__ == Directory
        )
        if item:
            return item
        else:
            return current_directory


FILE_REGEX = r"(\d*) (\S*)"


def parse_name(line: str, current_directory: Directory) -> SystemItem:
    if line[0:3] == "dir":
        return Directory(line[4:], [], current_directory)
    else:
        capture_groups = list(re.search(FILE_REGEX, line).groups())
        return File(capture_groups[1], int(capture_groups[0]))


def parse_line(line: str, current_directory: Directory) -> Directory:
    if len(line.strip()) == 0:
        return current_directory

    if line[0] == "$":
        return parse_command(line[2:], current_directory)
    else:
        current_directory.items.append(parse_name(line, current_directory))
        return current_directory


def get_directory_names_with_sizes(
    current_directory: Directory,
) -> List[Tuple[str, int]]:
    directories = [
        item for item in current_directory.items if item.__class__ == Directory
    ]
    result = []
    for directory in directories:
        result.append((directory.name, directory.get_size()))
        result = result + get_directory_names_with_sizes(directory)
    return result


def parse_and_build_top_level(lines: List[str]) -> Directory:
    starting = Directory("/", [], None)
    current_directory = starting
    for line in lines[1:]:
        current_directory = parse_line(line, current_directory)
    return starting


TOTAL_SIZE = 70000000
NEEDED_SIZE = 30000000


def part2(lines: List[str]) -> int:
    top_level = parse_and_build_top_level(lines)
    required = NEEDED_SIZE - TOTAL_SIZE + top_level.get_size()
    directories = get_directory_names_with_sizes(top_level)
    adequate_sizes = [size for directory, size in directories if size >= required]
    adequate_sizes.sort()
    return adequate_sizes[0]


def part1(lines: List[str]) -> int:
    top_level = parse_and_build_top_level(lines)

    directories = get_directory_names_with_sizes(top_level)
    return sum([size for directory, size in directories if size <= 100000])


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day7")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
