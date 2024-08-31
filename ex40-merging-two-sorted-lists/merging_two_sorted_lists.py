from collections import deque

def merge_two_lists(l1: list, l2: list) -> list:
    """
    Returns a sorted list of all numbers from two sorted lists of numbers.
    """
    if not l1:
        return l2
    if not l2:
        return l1
    
    l1, l2 = deque(l1), deque(l2)
    result = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            result.append(l1.popleft())
        else:
            result.append(l2.popleft())
    result.extend(l1)
    result.extend(l2)

    return result


assert merge_two_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert merge_two_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert merge_two_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert merge_two_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert merge_two_lists([1, 2, 3], []) == [1, 2, 3]
assert merge_two_lists([], [1, 2, 3]) == [1, 2, 3]
