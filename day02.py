from enum import Enum
from typing import Tuple

from utilities import file_handling


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(Enum):
    LOSE = 1
    DRAW = 2
    WIN = 3


THEIR_MOVES = {'A': Move.ROCK, 'B': Move.PAPER, 'C': Move.SCISSORS}
MY_MOVES = {'X': Move.ROCK, 'Y': Move.PAPER, 'Z': Move.SCISSORS}
MY_RESULTS = {'X': Result.LOSE, 'Y': Result.DRAW, 'Z': Result.WIN}


def move_from_string(line: str) -> Tuple[Move, Move]:
    return THEIR_MOVES[line[0]], MY_MOVES[line[2]]


def goal_from_string(line: str) -> Tuple[Move, Result]:
    return THEIR_MOVES[line[0]], MY_RESULTS[line[2]]


def work_out_move(result: Tuple[Move, Result]) -> Tuple[Move, Move]:
    them, desired_result = result
    if desired_result == Result.DRAW:
        return them, them
    elif desired_result == Result.WIN:
        if them != Move.SCISSORS:
            return them, Move(them.value + 1)
        else:
            return them, Move.ROCK
    else:
        if them != Move.ROCK:
            return them, Move(them.value - 1)
        else:
            return them, Move.SCISSORS


def score_move(move: Tuple[Move, Move]) -> int:
    them, me = move
    if them == me:
        return 3 + me.value
    elif (me == Move.SCISSORS and them == Move.ROCK) or (me != Move.SCISSORS and them == Move(me.value + 1)):
        return 0 + me.value
    else:
        return 6 + me.value


if __name__ == '__main__':
    data = file_handling.input_as_lines('data/day2')
    moves = map(move_from_string, data)
    scores = list(map(score_move, moves))
    print("Part1: ", sum(scores))
    goals = map(goal_from_string, data)
    moves_p2 = map(work_out_move, goals)
    scores_p2 = list(map(score_move, moves_p2))
    print("Part2: ", sum(scores_p2))


