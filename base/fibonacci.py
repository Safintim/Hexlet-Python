def fib_recursion(number: int) -> int:
    if number < 0:
        raise 'Need positive n'
    if number <= 1:
        return number
    return fib_recursion(number - 1) + fib_recursion(number - 2)


def fib_cycle(number: int) -> int:
    if number < 0:
        raise 'Need positive n'

    if number <= 1:
        return number

    f1 = 1
    f2 = 1
    for _ in range(2, number):
        current = f1 + f2
        f1 = f2
        f2 = current
    return f2
