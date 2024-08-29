def make_change(amount: int) -> dict:
    """
    Returns a special dictionary of
    minimum US coins for amount in cents.
    """
    # list of tuple coin types
    coins = [
        ('quarters', 25),
        ('dimes', 10),
        ('nickels', 5),
        ('pennies', 1),
    ]
    change = {}
    for denomination, value in coins:
        if amount >= value:
            # coins counted by floor division
            change[denomination] = amount // value
            # deduct amount by value of coins counted
            amount -= change[denomination] * value
    return change

assert make_change(30) == {'quarters': 1, 'nickels': 1}
assert make_change(10) == {'dimes': 1}
assert make_change(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert make_change(100) == {'quarters': 4}
assert make_change(125) == {'quarters': 5}
