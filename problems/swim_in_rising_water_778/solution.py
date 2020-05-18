from typing import List


def dijkstra(grid):
    grid_rows, grid_cols = len(grid), len(grid[0])
    node_pad = grid_rows * grid_cols
    distances = [node_pad for _ in range(grid_cols * grid_rows)]
    distances[0] = grid[0][0]
    visited = [False for _ in range(grid_cols * grid_rows)]

    for _ in range(grid_rows * grid_cols):
        unvisited_distances = [x if not visited[i] else float('inf') for i, x in enumerate(distances)]
        node_idx = unvisited_distances.index(min(unvisited_distances))
        node_c, node_r = node_idx % grid_cols, node_idx // grid_cols
        neighbors = [
            (node_r, node_c + 1),
            (node_r, node_c - 1),
            (node_r + 1, node_c),
            (node_r - 1, node_c)
        ]
        neighbors = [
            x for x in neighbors
            if (x[0] < grid_cols) and (x[0] >= 0) and (x[1] < grid_rows) and (x[1] >= 0)
        ]
        for n_r, n_c in neighbors:
            val_neighbor = grid[n_r][n_c]
            dist_neighbor = distances[n_r * grid_cols + n_c]
            dist_node = distances[node_r * grid_cols + node_c]
            distances[n_r * grid_cols + n_c] = max(val_neighbor, min(dist_neighbor, dist_node))
        visited[node_idx] = True

    return distances

def swim_in_water(grid: List[List[int]]) -> int:
    distances = dijkstra(grid)
    return distances[-1]