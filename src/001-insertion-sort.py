import time
from contextlib import contextmanager
from typing import Iterator

from rich import print
from rich.console import Console
from rich.table import Table
from rich.live import Live

console = Console()


def steps_table(all_steps: list):

    table = Table(show_footer=False)
    # table_centered = Align.center(table)

    console.clear()
    table = Table(title="Insertion sort", show_lines=True)
    table.add_column("key")
    table.add_column("i")
    table.add_column("j")

    for x in range(len(all_steps[0]) - 3):
        table.add_column(f"{str(x)}")
    for row in all_steps:
        table.add_row(*[str(r) for r in row])
    print(table)


def insertion_sort(numbers: list[int], print_steps: bool = False) -> None:
    """Given the initial array of numbers, We add the first number as initial number, then for each other number, we add in the correct place (read this as 'in between other two numbers')"""
    steps: list = []
    # sanity check for empty or arrays with one number
    if (n := len(numbers)) <= 1:
        return

    steps.append([None, None, None] + numbers.copy())
    # Using C-style code to implement the array loop```
    for i in range(1, n):
        # using name 'key like in the book'
        key = numbers[i]

        # we have to move all elements from numbers[0] until numbers[i-1] that are greater than 'key' one position to the 'right' to make space for the key to be placed
        j = i - 1
        steps.append([key, i, j] + numbers.copy())
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            steps.append([key, i, j] + numbers.copy())
            j -= 1
        numbers[j + 1] = key
        steps.append([key, i, j] + numbers.copy())

    if print_steps:
        steps_table(steps)


if __name__ == "__main__":
    unsorted = [4, 3, 2, 1]
    insertion_sort(unsorted, True)
