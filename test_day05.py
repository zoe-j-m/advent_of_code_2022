from day05 import part1, part2

test_lines = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split(
    "\n"
)


def test_part1():
    assert part1(test_lines) == 'CMZ'


def test_part2():
    assert part2(test_lines) == 'MCD'
