def draw_pyramid(height: int) -> None:
    """
    Draws a centered pyramid ASCII structure of '#'.
    """
    max_width = 2 * height - 1
    for row in range(height):
        print(' ' * (max_width - (2 * row + 1) // 2), end='')
        print('#' * (2 * row + 1), end='')
        print(' ' * (max_width - (2 * row + 1) // 2), end='')
        print()
