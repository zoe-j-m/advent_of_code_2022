from day16 import part1, part2, parse_to_valve, Valve


test_lines = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split(
    "\n"
)


def test_parse():
    valve = parse_to_valve(test_lines[0])
    print(valve.identifier, valve.rate, valve.links)
    assert valve == Valve("AA", 0, ["DD", "II", "BB"])
    valve = parse_to_valve(test_lines[7])
    print(valve.identifier, valve.rate, valve.links)
    assert valve == Valve("HH", 22, ["GG"])


def test_part1():
    assert part1(test_lines) == 1651


def test_part2():
    assert part2(test_lines) == 0
