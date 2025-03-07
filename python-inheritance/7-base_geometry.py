#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """A class to define geometric shapes."""

    def area(self):
        """Raises an exception as area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): name of the parameter.
            value (int): value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
