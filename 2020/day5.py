import sys
import re
import math


class BoardingPass:
    row_str = ""
    column_str = ""

    def __init__(self, raw_boarding_pass_string: str):
        self.row_str = raw_boarding_pass_string[0:7]
        self.column_str = raw_boarding_pass_string[7:10]

    def __str__(self):
        return self.row_str + " " + self.column_str

    def get_row_as_number(self) -> int:
        return self.parse_row(self.row_str)

    def get_seat_as_number(self) -> int:
        return self.parse_column(self.column_str)

    def parse_column(self, col: str) -> int:
        min_col = 0
        max_col = 7
        for i, c in enumerate(col):
            min_col, max_col = self.get_next_col(min_col, max_col, c)
        return min_col

    def get_next_col(self, min_col: int, max_col: int, character: str) -> (int, int):
        if character == "L":
            return min_col, math.floor((min_col + max_col) / 2)
        else:
            return math.ceil((min_col + max_col) / 2), max_col

    def get_next_row(self, min_row: int, max_row: int, character: str) -> (int, int):
        if character == "F":
            return min_row, math.floor((min_row + max_row) / 2)
        else:
            return math.ceil((min_row + max_row) / 2), max_row

    def parse_row(self, row: str) -> int:
        min_row = 0
        max_row = 127
        for i, c in enumerate(row):
            min_row, max_row = self.get_next_row(min_row, max_row, c)
        return min_row


if __name__ == "__main__":
    boarding_passes = []
    for line in sys.stdin:
        boarding_passes.append(BoardingPass(line.strip()))

    max_id = 0
    ids = []
    for board in boarding_passes:
        row = board.get_row_as_number()
        seat = board.get_seat_as_number()
        print("{:d} {:d}".format(row, seat))
        id = row * 8 + seat
        ids.append(id)
        max_id = max(max_id, id)

    print(max_id)
    ids.sort()
    print(ids)
    for i, id in enumerate(ids[0:-1]):
        if ids[i+1] - id > 1:
            print("my seat is ", id+1)


