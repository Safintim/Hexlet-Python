from collections import defaultdict


def make_user(name, age):
    return {'name': name, 'age': age}


def format_user(user):
    return f'{user['name']}, {user['age']}'


def count_all(iterable):
    d = {}
    for element in iterable:
        d[element] = d.get(element, 0) + 1
    return d


def collect_indexes(iterable):
    res = defaultdict(list)
    for i, item in enumerate(iterable):
        res[item].append(i)
    return res


def all_unique(iterator):
    items = list(iterable)
    return len(items) == len(set(items))


def toggle(flag, flags):
    if flag in flags:
        flags.discard(flag)
    else:
        flags.add(flag)


def toggled(flag, flags):
    copy_flags = flags.copy()
    toggle(flag, copy_flags)
    return copy_flags


def diff_keys(old, new):
    return {
        'kept': set(old) & set(new),
        'added': set(new) - set(old),
        'removed': set(old) - set(new),
    }


def apply_diff(target, diff):
    target.update(diff.get('add', set()))
    target.difference_update(diff.get('remove', set()))
