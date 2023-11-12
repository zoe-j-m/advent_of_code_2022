from day12 import part1, part2

test_lines = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split(
    "\n"
)


def test_part1():
    execute_lines = [line for line in test_lines]
    assert part1(execute_lines) == 31


def test_part2():
    assert part2(test_lines) == 29
