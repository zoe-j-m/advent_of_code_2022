from typing import List, Tuple

from utilities import file_handling

class Monkey:
    def __init__(self, starting_items: List[int], inspection_operation: str, inspection_amount: int, check_value: int, inspection_true_monkey: int, inspection_false_monkey: int):
        self.inspection_count = 0
        self.items = starting_items
        self.inspection_operation = inspection_operation
        self.inspection_amount = inspection_amount
        self.check_value = check_value
        self.inspection_true_monkey = inspection_true_monkey
        self.inspection_false_monkey = inspection_false_monkey

    def inspect(self, monkey_factor : int, simple_factor: bool) -> Tuple[int, int]:
        self.inspection_count += 1
        item = self.items.pop(0)
        if self.inspection_operation == 'sqr':
            item *= item
        elif self.inspection_operation == '*':
            item *= self.inspection_amount
        else:
            item += self.inspection_amount
        
        if simple_factor:
            item = item // monkey_factor
        else:
            if item > monkey_factor:
               item = monkey_factor + item % monkey_factor
        
        if item % self.check_value == 0:
            return (item, self.inspection_true_monkey)
        else:
            return (item, self.inspection_false_monkey)

    def __str__(self):
        return f"Monkey holds: {self.items}"


def turn(monkeys : List[Monkey], monkey_factor: int, simple_factor: bool):
    for monkey in monkeys:
        while monkey.items:
            item, give_to = monkey.inspect(monkey_factor, simple_factor)
            monkeys[give_to].items.append(item)

def parse_lines_to_monkey(lines: List[str]) -> Monkey:
    lines.pop(0) #Monkey Number Line, don't need
    
    starting_items_line = lines.pop(0)
    starting_items = list(map(int, starting_items_line[18:].split(",")))
    
    operation_line = lines.pop(0)[19:]
    if operation_line == "old * old":
        operation = 'sqr'
        operation_amount = 0
    else:
        operation = operation_line[4]
        operation_amount = int(operation_line[6:])

    check_value = int(lines.pop(0)[21:])

    true_monkey = int(lines.pop(0)[29:])

    false_monkey = int(lines.pop(0)[30:])

    if lines:
        lines.pop(0) # blank line between monkeys 
    
    return Monkey(starting_items, operation, operation_amount, check_value, true_monkey, false_monkey)

def lines_to_monkeys(lines : List[str]) -> List[Monkey]:
    monkeys = []
    while lines:
        monkeys.append(parse_lines_to_monkey(lines))     

    return monkeys


def monkey_chase(monkeys: List[Monkey], rounds: int, monkey_factor : int, simple_factor: bool) -> int:
    for i in range(rounds):
        turn(monkeys, monkey_factor, simple_factor)

    inspection_counts = [monkey.inspection_count for monkey in monkeys]

    inspection_counts = sorted(inspection_counts, reverse = True)
   
    return inspection_counts[0] * inspection_counts[1]


def part1(lines: List[str]) -> int:
    monkeys = lines_to_monkeys(lines)
    return monkey_chase(monkeys, 20, 3, True)


def part2(lines: List[str]) -> int:
    monkeys = lines_to_monkeys(lines)
    monkey_factor = 1
    for monkey in monkeys:
        monkey_factor *= monkey.check_value
    return monkey_chase(monkeys, 10000, monkey_factor, False)

if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day11")
    execute_lines = [line for line in data]
    print("Part1: ", part1(execute_lines))
    print("Part2: ", part2(data))