from typing import List, TypeVar, Tuple

T = TypeVar("T")


class Matrix:
    def __init__(self, rows: List[List[T]]):
        self.rows = rows

    def __getitem__(self, item) -> List[T]:
        return self.rows[item]

    def height(self) -> int:
        return len(self.rows)

    def width(self) -> int:
        if self.height() == 0:
            width = 0
        else:
            width = len(self.rows[0])
        return width

    def rotate_left(self):
        return Matrix(
            [
                [self.rows[j][i] for j in range(len(self.rows))]
                for i in range(len(self.rows[0]) - 1, -1, -1)
            ]
        )

    def transpose(self):
        return Matrix(
            [
                [self.rows[j][i] for j in range(len(self.rows))]
                for i in range(len(self.rows[0]))
            ]
        )

    def flatten(self):
        return [item for sublist in self.rows for item in sublist]

    def print(self):
        for x in self.rows:
            print(x)
