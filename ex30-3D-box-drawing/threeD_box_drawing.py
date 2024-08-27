def draw_box(size: int) -> None:
    """
    Draws a fixed 3D box design of a given size.
    """
    if size < 1:
        raise ValueError('Size must be 1 or more.')
    # one indexed
    # box top
    for i in range(1, size + 3):
        print(" " * (size - i + 2), end='')
        if i == 1:
            print("+" + '-' * (size * 2) + '+')
        elif i == size + 2:
            print("+" + '-' * (size * 2) + '+' + " " * (i - 2) + "+")
        else:
            print("/" + " " * (size * 2) + "/" + " " * (i - 2) + "|")
    # box front (beginning below edge)
    for i in range(1, size + 2):
        if i == size + 1:
            print('+' + '-' * (size * 2) + '+')
        else:
            print('|' + " " * (size * 2) + '|' + " " * (size - i) + "/")
