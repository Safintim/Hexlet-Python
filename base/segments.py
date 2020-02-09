def is_degenerated(line: tuple) -> bool:
    point1, point2 = line
    return point1 == point2


def is_vertical(line: tuple) -> bool:
    (point1_x, point1_y), (point2_x, point2_y) = line
    return point1_x == point2_x and point1_y != point2_y


def is_horizontal(line: tuple) -> bool:
    (point1_x, point1_y), (point2_x, point2_y) = line
    return point1_x != point2_x and point1_y == point2_y


def is_inclined(line: tuple) -> bool:
    (point1_x, point1_y), (point2_x, point2_y) = line
    return point1_x != point2_x and point1_y != point2_y
