def binary_sum(number1: str, number2: str) -> str:
    sum_numbers = int(number1, 2) + int(number2, 2)
    return bin(sum_numbers)[2:]
