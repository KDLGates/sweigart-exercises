def collatz(starting_number: int) -> list:
    """
    Returns a list of the Collatz sequence values for a starting number.
    """
    l = []
    if starting_number < 1:
        return l
    
    n = starting_number
    while True:
        if n == 1:
            l.append(n)
            return l
        if n % 2 == 0:
            l.append(n)
            n = n // 2
        else:
            l.append(n)
            n = 3 * n + 1


assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123

import random

random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum # Make sure it includes the starting number.
    assert seq[-1] == 1  # Make sure the last integer is 1.