import sys
from functools import reduce


def find_char_at_pos_wrap_around(line: str, pos: int) -> str:
    length = len(line)
    pos_on_line = pos % length
    return line[pos_on_line]


def is_tree(character: str) -> bool:
    return character == "#"


def get_trees_in_path(right: int, down: int, slopes: list) -> int:
    column = 0
    count = 0
    for line in slopes[::down]:
        if is_tree(find_char_at_pos_wrap_around(line, column)):
            count += 1
        column += right
    return count


if __name__ == "__main__":
    slope_map = []
    for line in sys.stdin:
        slope_map.append(line.strip())

    print(get_trees_in_path(3, 1, slope_map))

    # part 2
    angles = [{"right": 1, "down": 1}, {"right": 3, "down": 1}, {"right": 5, "down": 1}, {"right": 7, "down": 1},
              {"right": 1, "down": 2}]
    trees = []
    for angle in angles:
        trees.append(get_trees_in_path(angle["right"], angle["down"], slope_map))

    print(trees)
    print(reduce(lambda x, y: x * y, trees))
