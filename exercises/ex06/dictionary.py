"""Some dictionary functions!"""

__author__ = "730705250"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    output: dict[str, str] = {}

    for key in dictionary:
        new_key = dictionary[key]
        new_value = key  # Defining this variable just for clarity.

        if new_key in output:  # The key's already in the dictionary...
            raise KeyError("duplicate key in inverted dictionary!")
        else:
            output[new_key] = new_value

    return output


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the most frequently chosen color."""
    color_count: dict[str, int] = {}
    highest_value: int = 0
    highest_color: str = ""

    for person in dictionary:
        color = dictionary[person]

        if not (color in color_count):
            color_count[color] = 0

        color_count[color] += 1

        if color_count[color] > highest_value:
            highest_value = color_count[color]
            highest_color = color

    return highest_color


def count(words_list: list[str]) -> dict[str, int]:
    """Counts the occurences of words in a given list."""
    words_count: dict[str, int] = {}
    for word in words_list:
        if not (word in words_count):
            words_count[word] = 0
        words_count[word] += 1

    return words_count


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """Categorizes words by starting letter."""
    output: dict[str, list[str]] = {}

    for word in words_list:
        first_letter: str = word.lower()[0]
        if not (first_letter in output):
            output[first_letter] = []

        output[first_letter].append(word)

    return output


def update_attendance(attendance_log: dict[str, list[str]], day_of_week: str, student_name: str) -> dict[str, list[str]]:
    """Updates attendance log with attendance information. Mutates given dictionary."""
    if not (day_of_week in attendance_log):
        attendance_log[day_of_week] = []

    if not (student_name in attendance_log[day_of_week]):
        attendance_log[day_of_week].append(student_name)

    return attendance_log
