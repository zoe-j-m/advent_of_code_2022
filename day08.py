from typing import List, Tuple, Set, Dict

from utilities import file_handling

from utilities.matrices import Matrix

from functools import reduce


def lines_to_matrix(lines: List[str]) -> Matrix:
    return Matrix([[int(value) for value in line] for line in lines])


def check_visible(grid: Matrix, so_far: Set[Tuple[int, int]]):
    for row in grid.rows:
        highest = -1
        for value in row:
            height, coord_j, coord_i = value
            if height > highest:
                so_far.add((coord_j, coord_i))
                highest = height


def check_scenic(grid: Matrix, so_far: Dict[Tuple[int, int], List[int]]):
    for row_idx, row in enumerate(grid.rows):
        for col_idx, value in enumerate(row):
            height, coord_j, coord_i = value
            visible = 0
            scan_col = col_idx + 1
            while scan_col < len(row):
                scan_height = grid[row_idx][scan_col][0]
                visible += 1
                if scan_height >= height:
                    break
                scan_col += 1

            if (coord_j, coord_i) in so_far:
                so_far[(coord_j, coord_i)].append(visible)
            else:
                so_far[(coord_j, coord_i)] = [visible]


def add_coords(matrix: Matrix) -> Matrix:
    return Matrix(
        [
            [(height, row_idx, col_idx) for col_idx, height in enumerate(row)]
            for row_idx, row in enumerate(matrix.rows)
        ]
    )


def scenic_score_from_list(scores: List[int]) -> int:
    return reduce(lambda a, b: a * b, scores)


def part2(lines: List[str]) -> int:
    matrix = lines_to_matrix(lines)
    with_coords = add_coords(matrix)

    results_dict = {}
    for i in range(4):
        check_scenic(with_coords, results_dict)
        with_coords = with_coords.rotate_left()

    scenics = results_dict.values()

    scores = map(scenic_score_from_list, scenics)

    return max(scores)


def part1(lines: List[str]) -> int:
    matrix = lines_to_matrix(lines)
    with_coords = add_coords(matrix)
    results_set = set()
    for i in range(4):
        check_visible(with_coords, results_set)
        with_coords = with_coords.rotate_left()

    return len(results_set)


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day8")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
