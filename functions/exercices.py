import operator
from functools import reduce


def greet(name, *args):
    return 'Hello, {}!'.format(' and '.join((name, ) + args))


def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


def get_colors():
    return {
        'red': rgb(red=255),
        'green': rgb(green=255),
        'blue': rgb(blue=255)
    }


def updated(items, **kwargs):
    copies = items.copy()
    copies.update(kwargs)
    return copies


def call_twice(function, *args, **kwargs):
    res1 = function(*args, **kwargs)
    res2 = function(*args, **kwargs)
    return res1, res2


def filter_map(function, iterable):
    output = []
    for item in iterable:
        is_true, res = function(item)
        if is_true:
            output.append(res)
    return output


def keep_truthful(iterable):
    return filter(operator.truth, iterable)


def abs_sum(iterable):
    return sum(map(abs, iterable))


def walk(source, keys):
    return reduce(operator.getitem, keys, source)


def partial_apply(func, arg1):
    def inner(arg2):
        return func(arg1, arg2)
    return inner


def flip(func):
    def inner(arg1, arg2):
        return func(arg2, arg1)
    return inner


def make_module(step=1):
    return {
        'inc': lambda x: x + step,
        'dec': lambda x: x - step,
    }
