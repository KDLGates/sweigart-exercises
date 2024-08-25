import random

def roll_dice(dice:int) -> int:
    """
    Returns the sum of 6-sided dice of count dice.
    """
    if not dice:
        return 0
    if dice < 0:
        raise ValueError('`dice` must be positive.')
    total = 0
    for die in range(1, dice + 1):
        total += random.randint(1, 6)
    return total

assert roll_dice(0) == 0
assert roll_dice(1000) != roll_dice(1000)

for i in range(1000):
    assert 1 <= roll_dice(1) <= 6
    assert 2 <= roll_dice(2) <= 12
    assert 3 <= roll_dice(3) <= 18
    assert 100 <= roll_dice(100) <= 600
