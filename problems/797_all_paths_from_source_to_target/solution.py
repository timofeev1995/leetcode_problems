from typing import List, Tuple


def dfs(graph: List[List[int]], starting_node: int, path_accum: List[Tuple]) -> List[Tuple]:
    path_accum = [path + (starting_node,) for path in path_accum]
    if starting_node == len(graph) - 1:
        return path_accum
    else:
        neighbors = graph[starting_node]
        this_neighbor_paths = [dfs(graph, neighbor, path_accum) for neighbor in neighbors]
        return [item for paths in this_neighbor_paths for item in paths]


def all_paths_from_source_to_targets(graph: List[List[int]]) -> List[Tuple[int]]:
    return dfs(graph, 0, [()])


if __name__ == '__main__':
    g = [[1, 2], [3], [3], []]
    assert set(all_paths_from_source_to_targets(g)) == {(0, 1, 3), (0, 2, 3)}

    g = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    assert set(all_paths_from_source_to_targets(g)) == {(0, 4), (0, 3, 4), (0, 1, 3, 4), (0, 1, 2, 3, 4), (0, 1, 4)}

    g = [[4, 3, 1], [3, 2, 4], [], [4], []]
    assert set(all_paths_from_source_to_targets(g)) == {(0, 4), (0, 3, 4), (0, 1, 3, 4), (0, 1, 4)}
