from utilities import file_handling

if __name__ == '__main__':
    data = file_handling.input_as_lists_of_ints('data/day1')
    elves_carrying = list(map(sum, data))
    print("Part1: ", max(elves_carrying))
    elves_carrying.sort(reverse=True)
    print("Part2: ", sum(elves_carrying[:3]))

