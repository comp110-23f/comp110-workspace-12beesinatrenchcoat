"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730705250"


class Simpy:
    """Utility class for working with sequences of numerical data."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes the Simpy with a list of floats."""
        self.values = values

    def __str__(self) -> str:
        """Returns string in the format of 'Simpy([values])'."""
        return f"Simpy({self.values})"

    def fill(self, value: float, value_count: int) -> None:
        """Fills the Simpy with a number of repeating values. Mutates object."""
        new_values: list[float] = []
        for i in range(value_count):
            new_values.append(value)

        self.values = new_values

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the Simpy with a range of values."""
        assert step != 0.0  # Make sure we don't get stuck in an infinite loop.

        new_values: list[float] = []
        current: float = start

        # Absolute value, so the method still works with negative numbers
        while abs(current) < abs(stop):
            new_values.append(current)
            current += step

        self.values = new_values

    def sum(self) -> float:
        """Sums the values in the Simpy."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds corresponding values of Simpy objects together, or a single float to every value in a Simpy."""
        new_values: list[float] = []
        base_list: list[float] = self.values

        if isinstance(rhs, Simpy):
            other_values: list[float] = rhs.values
            # Ensure the lists are the same length
            assert len(base_list) == len(other_values)

            for i in range(0, len(base_list)):
                new_values.append(base_list[i] + other_values[i])

        elif isinstance(rhs, float):
            for value in base_list:
                new_values.append(value + rhs)

        return Simpy(new_values)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponentiates corresponding values of Simpy objects together, or a single float to every value in a Simpy."""
        new_values: list[float] = []
        base_list: list[float] = self.values

        if isinstance(rhs, Simpy):
            other_values: list[float] = rhs.values
            # Ensure the lists are the same length
            assert len(base_list) == len(other_values)

            for i in range(0, len(base_list)):
                new_values.append(base_list[i] ** other_values[i])

        elif isinstance(rhs, float):
            for value in base_list:
                new_values.append(value ** rhs)

        return Simpy(new_values)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks if all values in a Simpy are equal to all values in another Simpy or to a float, returns a list of booleans."""
        new_values: list[bool] = []
        base_list: list[float] = self.values

        if isinstance(rhs, Simpy):
            other_values: list[float] = rhs.values
            # Ensure the lists are the same length
            assert len(base_list) == len(other_values)

            for i in range(0, len(base_list)):
                new_values.append(base_list[i] == other_values[i])

        elif isinstance(rhs, float):
            for value in base_list:
                new_values.append(value == rhs)

        return new_values

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks if all values in a Simpy are greater than all values in another Simpy or to a float, returns a list of booleans."""
        new_values: list[bool] = []
        base_list: list[float] = self.values

        if isinstance(rhs, Simpy):
            other_values: list[float] = rhs.values
            # Ensure the lists are the same length
            assert len(base_list) == len(other_values)

            for i in range(0, len(base_list)):
                new_values.append(base_list[i] > other_values[i])

        elif isinstance(rhs, float):
            for value in base_list:
                new_values.append(value > rhs)

        return new_values

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Gets a specific item in Simpy.values, or filters Simpy.values (and returns a new Simpy)."""
        if isinstance(rhs, int):
            return self.values[rhs]

        if isinstance(rhs, list):
            new_values: list[float] = []

            for i in range(0, len(self.values)):
                if rhs[i]:
                    new_values.append(self.values[i])

            return Simpy(new_values)
