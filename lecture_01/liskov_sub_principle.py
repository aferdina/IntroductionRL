""" Liskov Substitution Principle
"""


class Rectangle:
    """Class to define a rectangle"""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: float) -> None:
        self.width = width

    def set_height(self, height) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height


def is_square(rc: Rectangle) -> bool:
    """check if the rectangle is a square

    Args:
        rc (Rectangle): rectangle object to check

    Returns:
        bool: true if it is a rectangle, false otherwise
    """
    return rc.width == rc.height


class Square(Rectangle):
    """class to define a square"""

    def __init__(self, width: float) -> None:
        super().__init__(width=width, height=width)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height


# The method ``is_square`` takes a Rectangle object and checks if it is a square.
# After the liskov substitution principle, we can use the ``is_square`` method with a
# Square object and get the desired behaviour.

if __name__ == "__main__":
    used_rc = Rectangle(2.0, 3.0)
    is_square(used_rc)
    print(f"used_sq is a square: {is_square(used_rc)}")

    used_sq = Square(5.0)
    print(f"used_sq is a square: {is_square(used_sq)}")
