"""A class representing a point in 2D space."""

from __future__ import annotations

__author__ = "730705250"


class Point:
    """A point in 2D space."""

    def __init__(self, x_init: float, y_init: float):
        """Initialization function: sets the x and y values of the point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Mutates the current point with scaled coordinates."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns a new point with scaled coordinates."""
        return Point(self.x * factor, self.y * factor)
