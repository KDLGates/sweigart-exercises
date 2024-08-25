def get_cost_of_coffee(coffees: int, price: float) -> float:
    """
    Every 9th coffee is free. Return the cost for count coffees of coffee.
    """
    if price < 0:
        raise ValueError('Coffee price must be positive.')
    cost = coffees * price
    cost -= (coffees // 9) * price
    return cost

assert get_cost_of_coffee(7, 2.50) == 17.50

assert get_cost_of_coffee(8, 2.50) == 20

assert get_cost_of_coffee(9, 2.50) == 20

assert get_cost_of_coffee(10, 2.50) == 22.50

 

for i in range(1, 4):

    assert get_cost_of_coffee(0, i) == 0

    assert get_cost_of_coffee(8, i) == 8 * i

    assert get_cost_of_coffee(9, i) == 8 * i

    assert get_cost_of_coffee(18, i) == 16 * i

    assert get_cost_of_coffee(19, i) == 17 * i

    assert get_cost_of_coffee(30, i) == 27 * i
    