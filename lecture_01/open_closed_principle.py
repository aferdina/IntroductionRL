""" Example for explaining SOLID principles from
https://dev.to/cleancodestudio/python-open-closed-design-pattern-python-solid-principles-1b5i
"""
from abc import ABC, abstractmethod
from typing import List

# pylint: disable=too-few-public-methods


class Shape(ABC):
    """Abstract class for shapes"""

    @abstractmethod
    def area(self):
        """calculate the area of a shape"""


def calculate_area(shapes: List[Shape]) -> float:
    """calculate the total area of a list of shapes

    Args:
        shapes (List[Shape]): list of shapes to calculate the area

    Returns:
        float: total area of the shapes
    """
    return sum(shape.area() for shape in shapes)


# In this example, the Shape class is an abstract base class that defines
# the interface for all shapes, and the Circle and Rectangle classes
# inherit from it and provide concrete implementations of the area method.
# The calculate_area function takes a list of shapes and
# calculates the total area by calling the area method on each shape.

class Circle(Shape):
    """Class to define a circle"""

    def __init__(self, radius: float) -> None:
        """intialize the radius of the circle

        Args:
            radius (float): radius of the circle
        """
        self.radius = radius

    def area(self) -> float:
        """calculate area of the circle

        Returns:
            float: area of the circle
        """
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    """Class to define a rectangle"""

    def __init__(self, width: float, height: float) -> None:
        """intialize the width and height of the rectangle

        Args:
            width (float): width of the rectangle
            height (float): height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """calculate area of the rectangle

        Returns:
            float: area of the rectangle
        """
        return self.width * self.height


# By using inheritance and an abstract base class, the existing code can be
# extended to support new shapes without having to modify the existing code.
# For example, if we wanted to add a square shape, we could simply
# create a Square class that inherits from Shape and provide an implementation of the area method.
# This adheres to the Open/Closed Principle as the existing code
# remains closed for modification, while new functionality can be added through extension.

if __name__ == "__main__":
    used_shapes = [Circle(2), Rectangle(2, 4), Circle(4), Rectangle(4, 8)]
    print(f"Total area: {calculate_area(used_shapes)}")
