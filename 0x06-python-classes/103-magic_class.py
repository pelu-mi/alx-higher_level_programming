#!/usr/bin/python3
"""Module description goes here"""


class MagicClass:
    """Class Description goes here"""

    def __init__(self, radius=0):
        """Initialize MagicClass"""
        self._MagicClass__radius = 0
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Return Area of the MagicClass"""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Return Circumference of the MagicClass"""
        return 2 * math.pi * self._MagicClass__radius
