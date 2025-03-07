#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """A class to define geometric shapes."""

    def area(self):
        """Method that raises an exception as area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: if value is not exactly an int.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
