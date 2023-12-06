"""Dictionary related utility functions."""

__author__ = "730705250"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Make a list of all values in a given column."""
    values: list[str] = []
    for row in table:
        values.append(row[key])

    return values


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table from a list of rows into a dictionary of columns."""
    output: dict[str, list[str]] = {}
    for column in table[0].keys():
        output[column] = column_values(table, column)

    return output


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Create a new column-based table with a specified number of rows."""
    # This kinda mashes column_values and columnar together.
    if rows > len(table):
        print("Row count higher than table row count, returning entire table!")
        rows = len(table)

    output: dict[str, list[str]] = {}
    for column in table.keys():
        values: list[str] = []
        for row in range(0, rows):
            values.append(table[column][row])

        output[column] = values

    return output


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Create a new column-based table with a subset of columns."""
    output: dict[str, list[str]] = {}
    for column in columns:
        output[column] = table[column]

    return output


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column-based tables."""
    output: dict[str, list[str]] = {}
    for column in table1.keys():
        output[column] = table1[column]

    for column in table2.keys():
        if column in output:
            output[column] += table2[column]
        else:
            output[column] = table2[column]

    return output


def count(values: list[str]) -> dict[str, int]:
    """Counts the occurances of values in a list."""
    # Hey, wait, didn't we do this in that dictionary exercise?
    output: dict[str, int] = {}

    for value in values:
        if value not in output:
            # Add the key if it doesn't exist.
            output[value] = 0

        output[value] += 1

    return output
