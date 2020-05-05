from typing import List


def inverse_row(row: List[int]) -> List[int]:
    """

    :param row: `List[int]` to be inversed
    :return: `List[int]` inversed row
    """
    return [0 if x == 1 else 1 for x in row]


def increment_memory_state(memory: dict, element: List[int]):
    tuple_element = tuple(element)
    if tuple_element in memory:
        memory[tuple_element] += 1
    else:
        memory[tuple_element] = 1
    return memory


def max_equal_rows_after_flips(matrix: List[List[int]]) -> int:
    """

    :param matrix: `List[List[int]]` has elements 0 and 1
    :return: `int` number of rows which are equal after flops.
    """
    memory = {}
    for row in matrix:
        memory = increment_memory_state(memory, row)
        memory = increment_memory_state(memory, inverse_row(row))
    return max([v for v in memory.values()])



