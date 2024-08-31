def bubble_sort(numbers: list) -> list:
    """
    Bubblesorts a list of numbers in place and returns it.
    """
    def swap(l, a, b):
        c = l[a]
        l[a] = l[b]
        l[b] = c

    if len(numbers) <= 1:
        return numbers

    for i in range(len(numbers)):
        for j in range(i, len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                swap(numbers, j, j + 1)
    
    return numbers


assert bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2]
