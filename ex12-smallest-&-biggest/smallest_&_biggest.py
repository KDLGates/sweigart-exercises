import sys, random

def get_smallest(numbers: list) -> int|float:
    """
    Takes a list of ints and/or floats. Returns the smallest value.
    """
    if len(numbers) == 0:
        return None
    min = sys.maxsize
    for n in numbers:
        if n < min:
            min = n
    return min

def get_biggest(numbers: list) -> int | float:
    """
    Takes a list of ints and/or floats. Returns the biggest value.
    """
    if len(numbers) == 0:
        return None
    max = sys.maxsize * -1
    for n in numbers:
        if n > max:
            max = n
    return max

assert get_smallest([1, 2, 3]) == 1
assert get_smallest([3, 2, 1]) == 1
assert get_smallest([28, 25, 42, 2, 28]) == 2
assert get_smallest([1]) == 1
assert get_smallest([]) == None

numbers = []

for i in range(1000000):
    numbers.append(random.randint(1, 1000000000))

print('Numbers:', numbers)
print('Smallest number is', get_smallest(numbers))
