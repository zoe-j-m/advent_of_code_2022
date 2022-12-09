from day08 import part1, part2

test_lines = """30373
25512
65332
33549
35390""".split(
    "\n"
)


def test_part1():
    assert part1(test_lines) == 21


def test_part2():
    assert part2(test_lines) == 8
