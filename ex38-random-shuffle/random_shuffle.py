import random

def shuffle(values: list) -> list:
    """
    Takes a list of integers and returns a new permutation of its values.
    """
    pass

    def swapElements(l, a, b):
        c = l[a]
        l[a] = l[b]
        l[b] = c

    if not values:
        return []
    
    for i in range(len(values)):
        while True:
            j = random.randint(0, len(values) - 1)
            if j == i:
                continue
            else:
                break
        swapElements(values, i, j)
    
    return values

def fisher_yates_shuffle(values: list) -> None:
    """
    Uses the Fisher-Yates shuffle algorithm to concisely shuffle 
    a list in place into a permutation.
    """
    # i in range of result length last index descending to second-to-last
    for i in range(len(values) - 1, 0, -1):
        j = random.randint(0, i) # inclusive of endpoint
        values[i], values[j] = values[j], values[i] # eloquent swap

random.seed(42)


# Assertions


# Perform this test ten times:

for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fisher_yates_shuffle(testData1)
    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10
    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Make sure an empty list fisher_yates_shuffled remains empty:
testData2 = []
fisher_yates_shuffle(testData2)
assert testData2 == []