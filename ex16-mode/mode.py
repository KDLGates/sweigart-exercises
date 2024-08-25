def mode(numbers:list ) -> int|float|list:
    """
    Returns the mode of a list.
    """
    if not numbers:
        return None
    results = {}
    for n in numbers:
        if n not in results:
            results[n] = 1
        else:
            results[n] += 1
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    max = sorted_results[0][1]
    contenders = [key for key, freq in sorted_results if freq == max]
    if len(contenders) == 1:
        return contenders[0]
    else:
        return contenders

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4
