from day03 import part1, part2

test_lines = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split("\n")

def test_part1():
    assert part1(test_lines) == 157

def test_part2():
    assert part2(test_lines) == 70
