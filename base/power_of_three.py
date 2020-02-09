def is_power_of_three(number: int) -> bool:
    for degree in range(number):
        if 3 ** degree == number:
            return True
    return False
