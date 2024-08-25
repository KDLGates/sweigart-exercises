def calculate_sum(numbers: list) -> int|float:
    """
    Calculates a list's sum through repeated addition.
    """
    result = 0
    for num in numbers:
        result += num
    return result

def calculate_product(numbers: list) -> int|float:
    """
    Calculates a list's product through repeated multiplication.
    """
    result = 1
    for num in numbers:
        result *= num
    return result

assert calculate_sum([]) == 0
assert calculate_sum([2, 4, 6, 8, 10]) == 30
assert calculate_product([]) == 1
assert calculate_product([2, 4, 6, 8, 10]) == 3840
