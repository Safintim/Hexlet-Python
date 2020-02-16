def compose(func1, func2):
    def inner(arg):
        return func1(func2(arg))
    return inner


def find_index_of_nearest(number, source):
    if source:
        diff = list(map(lambda x: abs(x - number), source))
        return diff.index(min(diff))
