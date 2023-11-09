"""A class representing a point in 2D space."""

from __future__ import annotations

__author__ = "730705250"


class Point:
    """A point in 2D space."""

    x: int | float
    y: int | float

    def __init__(self, x_init: int | float = 0.0, y_init: int | float = 0.0):
        """Initialization function: sets the x and y values of the point."""
        self.x = x_init
        self.y = y_init

    def __str__(self) -> str:
        """Returns coordinates of point."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int | float) -> Point:
        """Returns new point with scaled coordinates; same as Point#scale()."""
        return self.scale(factor)

    def __add__(self, amount: int | float) -> Point:
        """Returns new point with incremented coordinates; same as Point#add()."""
        return self.add(amount)

    def scale_by(self, factor: int):
        """Mutates the current point with scaled coordinates."""
        self.x *= factor
        self.y *= factor

    def add(self, amount: int | float) -> Point:
        """Returns a new point with incremented coordinates."""
        return Point(self.x + amount, self.y + amount)

    def scale(self, factor: int | float) -> Point:
        """Returns a new point with scaled coordinates."""
        return Point(self.x * factor, self.y * factor)
