def inverted_right_angled_triangle(levels):
    """Prints an inverted right-angled triangle of stars."""
    for i in range(levels, 0, -1):
        print("* " * i)

# Example Usage
inverted_right_angled_triangle(8)
