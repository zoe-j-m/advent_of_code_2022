from typing import List, Tuple, TypeAlias, Set

from utilities import file_handling

from utilities.matrices import Matrix

Coords: TypeAlias = Tuple[int, int]


def findStart(grid: Matrix) -> Coords:
    for row_idx, row in enumerate(grid.rows):
        for col_idx, col in enumerate(row):
            if grid.rows[row_idx][col_idx] == "S":
                return (row_idx, col_idx)


def findEnd(grid: Matrix) -> Coords:
    for row_idx, row in enumerate(grid.rows):
        for col_idx, col in enumerate(row):
            if grid.rows[row_idx][col_idx] == "E":
                return (row_idx, col_idx)


def height_of(square: str) -> str:
    if square == "S":
        return "a"
    elif square == "E":
        return "z"
    else:
        return square


def moves_from(coord: Coords, grid: Matrix) -> List[Coords]:
    max_col = grid.width() - 1
    max_row = grid.height() - 1
    return [
        (row, col)
        for row in range(coord[0] - 1, coord[0] + 2)
        for col in range(coord[1] - 1, coord[1] + 2)
        if row > -1
        and row <= max_row
        and col > -1
        and col <= max_col
        and (row == coord[0] or col == coord[1])
    ]


def generate_candidates(
    previously_visited: Set[Tuple[int, int]],
    previous_candidates: List[List[Coords]],
    grid: Matrix,
    invert: bool,
) -> List[List[Coords]]:
    new_candidates = []
    for candidate in previous_candidates:
        prev_square = grid.rows[candidate[-1][0]][candidate[-1][1]]
        height_from = height_of(prev_square)
        possible_moves = moves_from(candidate[-1], grid)
        for move in possible_moves:
            this_height = height_of(grid.rows[move[0]][move[1]])
            if move not in previously_visited and (
                not invert
                and ord(this_height) - ord(height_from) < 2
                or invert
                and ord(height_from) - ord(this_height) < 2
            ):
                previously_visited.add(move)
                new_candidate = candidate.copy()
                new_candidate.append(move)
                new_candidates.append(new_candidate)
    return new_candidates


def part1(lines: List[str]) -> int:
    grid = Matrix(lines)
    start = findStart(grid)
    goal = findEnd(grid)
    print(goal)
    visited = set([start])
    candidate_solutions = [[start]]
    win = False
    result = 0
    while not win:
        assert candidate_solutions
        candidate_solutions = generate_candidates(
            visited, candidate_solutions, grid, False
        )
        for solution in candidate_solutions:
            if solution[-1] == goal:
                win = True
                result = len(solution) - 1  # moves not squares

    return result


def part2(lines: List[str]) -> int:
    grid = Matrix(lines)
    start = findEnd(grid)
    visited = set([start])
    candidate_solutions = [[start]]
    win = False
    result = 0
    while not win:
        assert candidate_solutions
        candidate_solutions = generate_candidates(
            visited, candidate_solutions, grid, True
        )
        for solution in candidate_solutions:
            if height_of(grid.rows[solution[-1][0]][solution[-1][1]]) == "a":
                win = True
                result = len(solution) - 1  # moves not squares

    return result


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day12")
    execute_lines = [line for line in data]
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
