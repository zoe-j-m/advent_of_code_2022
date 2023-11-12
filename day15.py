from typing import List, TypeAlias, Tuple, Set
from utilities import file_handling
import re

REGEX = r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)"

Coords: TypeAlias = Tuple[int, int]


def parse_to_coords(input: str) -> List[Tuple[Coords,Coords]]:
    matches = re.findall(REGEX, input)
    sensors_and_beacons = []
    for match in matches:
        sensors_and_beacons.append(((int(match[0]), int(match[1])), (int(match[2]), int(match[3]))))
    return sensors_and_beacons

def calculate_manhattan(coord1 : Coords, coord2: Coords) -> int:
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def generate_missing_beacons(sensor: Coords, which_row : int, manhattan_distance: int) -> Set[int]:
    y_offs = abs(sensor[1] - which_row)
    if  y_offs <= manhattan_distance: 
        return set([x for x in range(sensor[0] - manhattan_distance + y_offs, sensor[0] + manhattan_distance - y_offs + 1 )])
    else: 
        return set()
    

def part1(lines: List[str], which_row : int) -> int:
    sensors_and_beacons = [parse_to_coords(line)[0] for line in lines]
    no_beacons = set()
    sensor_beacon_manhattan = [(sensor, beacon, calculate_manhattan(sensor, beacon)) for (sensor, beacon) in sensors_and_beacons]
    for (sensor, beacon, manhattan) in sensor_beacon_manhattan:
        this_voids = generate_missing_beacons(sensor, which_row, manhattan)
        if sensor[1] == which_row:
            this_voids.remove(sensor[0])
        if beacon[1] == which_row:
            this_voids.remove(beacon[0])
        no_beacons = no_beacons.union(this_voids)
    return len(no_beacons)
  

def generate_possible_beacons(sensor: Coords, manhattan : int, max_x: int) -> Set[Coords]:
    minx = max([sensor[0] - manhattan,0])
    maxx = min([sensor[0] + manhattan, max_x])
    results = set()
    for x in range (minx, maxx + 1):
        y_val = sensor[1] + manhattan - abs(sensor[0] - x)
        if y_val > 0 and y_val <= max_x:
            results.add((x, y_val ))
        y_val = sensor[1] - manhattan + abs(sensor[0] - x)
        if y_val >= 0 and y_val <= max_x:
            results.add((x, y_val ))
    return results

def part2(lines: List[str], max_x : int) -> int:
    sensors_and_beacons = [parse_to_coords(line)[0] for line in lines]
    sensor_beacon_manhattan = [(sensor, beacon, calculate_manhattan(sensor, beacon)) for (sensor, beacon) in sensors_and_beacons]
    results = set()
    for (sensor, beacon, manhattan) in sensor_beacon_manhattan:
        this_possibility = generate_possible_beacons(sensor, manhattan + 1, max_x)
        results = results.union(this_possibility)
        print(sensor, manhattan + 1, len(this_possibility))
        for possibility in this_possibility:       
            for (sensor1, beacon1, manhattan1) in sensor_beacon_manhattan:
                if sensor1 == sensor:
                    continue
                if calculate_manhattan(sensor1, possibility) <= manhattan1:
                    results.remove(possibility)
                    break

    for (sensor, beacon, manhattan) in sensor_beacon_manhattan:            
        if sensor in results:
            results.remove(sensor)
        if beacon in results:
            results.remove(beacon)
    
    print(results)
    candidate = list(results)[0]
    return candidate[0] *  4000000 + candidate[1]


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day15")

    print("Part1: ", part1(data, 2000000))
    print("Part2: ", part2(data, 4000000))
