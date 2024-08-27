def draw_rectangle(width: int, height: int) -> None:
    """
    Prints a width x height rectangle of ASCII '#'.
    """
    for row in range(height):
        for col in range(width):
            print('#', end='')
        print()
