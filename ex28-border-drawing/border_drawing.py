def draw_border(width: int, height: int) -> None:
    """
    Draws ascii art of a rectangle border of width x height.
    """
    if width < 2 or height < 2:
        return
    
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1:
                if col == 0 or col == width - 1:
                    print('+', end='')
                else:
                    print('-', end='')
            elif col == 0 or col == width - 1:
                    print('|', end='')
            else:
                print(' ', end='')
        print()
