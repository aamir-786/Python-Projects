def hollow_symmetric_triangle(levels):
    """Prints a symmetric hollow star triangle pattern."""
    for i in range(levels):
        if i == levels - 1:
            print("*" * (2 * levels - 1))  # Last row is filled with stars
        else:
            print(" " * (levels - i - 1) + "*" + " " * (2 * i - 1) + ("*" if i > 0 else ""))

# Example Usage
hollow_symmetric_triangle(6)
