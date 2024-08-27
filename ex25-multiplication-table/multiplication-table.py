def print_multiplication_table() -> None:
    """
    Prints a fixed multiplication table for 1x1 through 10x10
    """
    header = "  | " + " ".join(f"{n:2d}" for n in range(1, 10))
    header += f" {10:>3d}" # special padding for 3-digit 10*10
    print(header)
    print("-" * (len(header) + 1))
    
    for i in range(1, 11):
        row = f"{i:2d}| " + " ".join(f"{i*j:2d}" for j in range(1, 10))
        row += f" {i*10:>3d}" # special padding for 3-digit 10*10
        print(row)
