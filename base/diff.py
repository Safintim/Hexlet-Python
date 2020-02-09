def diff(number1: int, number2: int) -> int:
    first = abs(number2 - number1)
    second = 360 - max(number1, number2) + min(number1, number2)
    return min(first, second)

"""
def diff(angle1, angle2):
    return min(
        (angle1 - angle2) % 360,
        (angle2 - angle1) % 360,
    )
"""