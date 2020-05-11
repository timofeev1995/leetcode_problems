from typing import List, Set


def dfs(idx, matrix: List[List[int]], visited: Set):
    for i, friend in enumerate(matrix[idx]):
        if friend and i not in visited:
            visited.add(i)
            visited = dfs(i, matrix, visited)
    return visited


def find_circle_num(matrix: List[List[int]]) -> int:
    unvisited = set(range(len(matrix)))
    visited = set()
    circles = 0
    while len(unvisited) > 0:
        idx = (unvisited - visited).pop()
        new_visited = dfs(idx, matrix, visited)

        visited.update(new_visited)
        unvisited -= new_visited
        circles += 1

    return circles



