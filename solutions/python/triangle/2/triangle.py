"""Module to determine triangle types based on side lengths."""

def equilateral(sides):
    """Return True if the triangle is equilateral."""
    side_one, side_two, side_three = sides

    if side_one <= 0 or side_two <= 0 or side_three <= 0:
        return False

    if side_one + side_two < side_three or side_two + side_three < side_one or side_one + side_three < side_two:
        return False

    return side_one == side_two == side_three


def isosceles(sides):
    """Return True if the triangle is isosceles."""
    side_one, side_two, side_three = sides

    if side_one <= 0 or side_two <= 0 or side_three <= 0:
        return False

    if side_one + side_two < side_three or side_two + side_three < side_one or side_one + side_three < side_two:
        return False

    return side_one == side_two or side_two == side_three or side_one == side_three


def scalene(sides):
    """Return True if the triangle is scalene."""
    side_one, side_two, side_three = sides

    if side_one <= 0 or side_two <= 0 or side_three <= 0:
        return False

    if side_one + side_two < side_three or side_two + side_three < side_one or side_one + side_three < side_two:
        return False

    return side_one != side_two and side_two != side_three and side_one != side_three