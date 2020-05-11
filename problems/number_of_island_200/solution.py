from typing import List


def dfs(i: int, j: int, grid: List[List[str]]):
    grid_condition = (i >= 0) and (i < len(grid)) and (j >= 0) and (j < len(grid[0]))
    grid_condition = grid_condition and (grid[i][j] == '1')
    if grid_condition:
        grid[i][j] = '0'
        dfs(i + 1, j, grid)
        dfs(i - 1, j, grid)
        dfs(i, j + 1, grid)
        dfs(i, j - 1, grid)


def num_islands(grid: List[List[str]]) -> int:
    """

    :param grid: List[List[str]] with `0` - water, `1` - ground
    """
    if not grid:
        return 0

    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j, grid)
                islands += 1
    return islands


