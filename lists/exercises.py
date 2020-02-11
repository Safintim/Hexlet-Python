import math


def get_square_roots(n):
    if n == 0: 
        return [0]
    elif n < 0:
        return []
    root = math.sqrt(n)
    return [-root, root]


def get_range(n):
    if n <= 0:
        return []

    index = 0
    output = []
    while index < n:
        output.append(index)
        index += 1
    return output


def duplicate(items):
    items.extend(items)


def rotate(items):
    if items:
        items.insert(0, items.pop())


def rotated_left(iterable):
    return iterable[1:] + iterable[:1]


def rotated_right(iterable):
    return iterable[-1:] + iterable[:-1]


def find_index(value, iterable):
    for index, element in enumerate(iterable):
        if value == element:
            return index


def find_second_index(value, iterable):
    iterator = iter(iterable)
    first_index = find_index(value, iterator)
    second_index = find_index(value, iterator)
    if second_index is not None:
        return second_index + first_index + 1
