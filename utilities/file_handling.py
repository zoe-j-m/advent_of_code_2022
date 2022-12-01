from typing import List


def input_as_string(filename: str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")


def input_as_ints_from_single_line(filename: str) -> List[int]:
    """returns the single line as a list of ints"""
    return list(map(lambda x: int(x), input_as_string(filename).split(',')))


def input_as_lines(filename: str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")


def line_as_int(line: str) -> int:
    return int(line.rstrip('\n'))


def input_as_ints(filename: str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    return list(map(line_as_int, lines))


def input_as_lists_of_ints(filename: str) -> List[List[int]]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)

    result = []

    current = []

    for line in lines:
        if len(line) == 0:
            result.append(current)
            current = []
        else:
            current.append(line_as_int(line))

    if len(current) > 0:
        result.append(current)

    return result
