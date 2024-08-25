def is_odd(n: int|float) -> bool:
    """Returns whether n is odd."""
    if n % 1 != 0:
        return False
    return not n % 2 == 0

def is_even(n: int|float) -> bool:
    """Returns whether n is even."""
    if n % 1 != 0:
        return False
    return n % 2 == 0

assert is_odd(42) == False
assert is_odd(9999) == True
assert is_odd(-10) == False
assert is_odd(-11) == True
assert is_odd(3.1415) == False
assert is_even(42) == True
assert is_even(9999) == False
assert is_even(-10) == True
assert is_even(-11) == False
assert is_even(3.1415) == False
