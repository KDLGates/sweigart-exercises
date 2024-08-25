def area(length, width):
    """Returns the area of a square."""
    if any(locals()) < 0:
        raise ValueError("Geometric values can't be negative.")
    return length * width

def perimeter(length, width):
    """Returns the perimeter of a square."""
    if any(locals()) < 0:
        raise ValueError("Geometric values can't be negative.")
    return 2 * length + 2 * width

def volume(length, width, height):
    """Returns the volume of a cube."""
    if any(locals()) < 0:
        raise ValueError("Geometric values can't be negative.")
    return length * width * height

def surface_area(length, width, height):
    """Returns the surface area of a cube."""
    if any(locals()) < 0:
        raise ValueError("Geometric values can't be negative.")
    # Surface area is the sum of pairs of opposing side areas of the cube.
    return (2 * length * width) + (2 * length * height) + (2 * width * height)

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surface_area(10, 10, 10) == 600
assert surface_area(9999, 0, 9999) == 199960002
assert surface_area(5, 8, 10) == 340