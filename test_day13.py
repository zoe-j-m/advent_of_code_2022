from day13 import part1, part2, parse_to_item

test_lines = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split(
    "\n"
)


def test_part1():
    print(parse_to_item(test_lines[0]))
    assert part1(test_lines) == 13


def test_part2():
    assert part2(test_lines) == 140
