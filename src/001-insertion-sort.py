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

    # console.clear()
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
    for j in range(1, n):
        # using name 'key like in the book'
        key = numbers[j]

        # ? we have to move all elements from numbers[0] until numbers[i-1] that are greater than 'key' one position to the 'right' to make space for the key to be placed
        # * In practice, we save the value of the number to be inserted, and keep copying values to the 'right'until
        # * we find the correct spot to place the number
        i = j - 1
        steps.append([key, i, j] + numbers.copy())
        while i >= 0 and key < numbers[i]:
            numbers[i + 1] = numbers[i]
            steps.append([key, i, j] + numbers.copy())
            i -= 1
        numbers[i + 1] = key
        steps.append([key, i, j] + numbers.copy())

    if print_steps:
        steps_table(steps)


if __name__ == "__main__":
    lists = [
        [4, 3, 2, 1],
        [1, 2, 3, 4],
        [9, 1, 8, 2, 7, 3, 6, 4, 5],
    ]
    for unsorted in lists:
        insertion_sort(unsorted, True)
