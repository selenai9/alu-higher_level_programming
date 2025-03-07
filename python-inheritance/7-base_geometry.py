#!/usr/bin/python3
"""Class that defines the attributes of Geometric Shapes."""


class BaseGeometry:
    """Class that defines the attributes of Geometric Shapes."""

    def area(self):
        """Method that defines the area of a geometric shape."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that receives the value property.

        Args:
            name (str): name of the object.
            value (int): value of the property.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
