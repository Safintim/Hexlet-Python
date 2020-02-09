def rotate_left(triple: tuple) -> tuple:
    a, b, c = triple
    return b, c, a


def rotate_right(triple: tuple) -> tuple:
    a, b, c = triple
    return c, a, b
