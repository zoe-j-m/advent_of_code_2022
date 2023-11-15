from typing import List, Dict, Optional, Tuple
from utilities import file_handling
import re
import itertools


class Valve:
    def __init__(self, identifier, rate, links):
        self.identifier = identifier
        self.rate = rate
        self.links = links

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return (
                self.identifier == other.identifier
                and self.rate == other.rate
                and self.links == other.links
            )
        return False


REGEX = r"Valve (\w{2}) has flow rate=(\d+); tunnel(?:s)? lead(?:s)? to valve(?:s)? ((\w{2}(?:,\s)?)+)"


def parse_to_valve(line: str) -> Valve:
    match = re.search(REGEX, line)
    identifier = match[1]
    rate = int(match[2])
    links = match[3].split(", ")
    return Valve(identifier, rate, links)


def calc_best_route(
    routes: List[List[str]], valves_dict: Dict[str, Valve], target_valve: str
) -> List[str]:
    new_routes = []
    for route in routes:
        from_val = valves_dict[route[0]]
        if target_valve in from_val.links:
            route.insert(0, target_valve)
            return route

        if not from_val.links:
            continue

        for valve in from_val.links:
            new_route = route.copy()
            new_route.insert(0, valve)
            new_routes.append(new_route)
    return calc_best_route(new_routes, valves_dict, target_valve)


def best_target(
    valves_list: List[Valve],
    valves_dict: Dict[str, Valve],
    route_costs: Dict[(str, str), int],
    current_valve: str,
    open_valves: List[str],
    time_remaining: int,
) -> Optional[Tuple[Valve, int]]:
    scoring_valves = list(
        filter(lambda x: x.rate > 0 and x.identifier not in open_valves, valves_list)
    )
    potentials = []
    for scoring_valve in scoring_valves:
        route_cost = route_costs[(current_valve, scoring_valve.identifier)]
        if route_cost and route_cost < time_remaining:
            # print(scoring_valve.identifier, best_route)
            potentials.append((scoring_valve, len(best_route)))
    sorted_pots = sorted(
        potentials,
        key=lambda a: a[0].rate * (time_remaining - (a[1])),
        reverse=True,
    )
    for potential in sorted_pots:
        print(
            "pot",
            potential[0].identifier,
            potential[0].rate * (time_remaining - (potential[1])),
        )
    if sorted_pots:
        return sorted_pots[0]
    else:
        return None


def part1(lines: List[str]) -> int:
    valves_list = list(map(parse_to_valve, lines))
    valves_dict = dict([(valve.identifier, valve) for valve in valves_list])
    time_remaining = 30
    open_valves = []
    valve_combos = list(itertools.combinations(valves_list, 2))
    route_costs = dict(
        map(lambda vc: (vc, calc_best_route(vc[0], valves_dict, vc[1])), valve_combos)
    )
    best_t = best_target(
        valves_list, valves_dict, route_costs, "AA", open_valves, time_remaining
    )
    score = 0
    while best_t:
        print(
            best_t[0].identifier,
            time_remaining - best_t[1],
            best_t[0].rate * (time_remaining - best_t[1]),
        )
        score += best_t[0].rate * (time_remaining - best_t[1])
        time_remaining -= best_t[1]
        open_valves.append(best_t[0].identifier)
        best_t = best_target(
            valves_list, valves_dict, best_t[0].identifier, open_valves, time_remaining
        )
    return score
    # solutions = do_generations(valves_dict, 30)
    # for solution in solutions:
    #     print(solution.score, solution.open_valves, solution.history)
    # return max(list(map(lambda solution: solution.score, solutions)))


def part2(lines: List[str]) -> int:
    return 0


data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
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


if __name__ == "__main__":
    # data = file_handling.input_as_lines("data/day16")
    print("Part1: ", part1(data))
# print("Part2: ", part2(data))
