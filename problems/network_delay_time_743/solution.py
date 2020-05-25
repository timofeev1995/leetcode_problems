from typing import List, Dict, Tuple


def make_nodemap(times: List[List[int]], N: int):
    nodemap = {i: [] for i in range(1, N + 1)}
    for u, v, w in times:
        nodemap[u].append((v, w))
    return nodemap


def dijkstra(nodemap: Dict[int, List[Tuple[int]]], k: int, n: int):
    visited = [False for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    d[k-1] = 0
    for _ in range(n):
        d_ = [x if not visit else float('inf') for x, visit in zip(d, visited)]
        min_index = d_.index(min(d_))
        visited[min_index] = True
        for (v, w) in nodemap[min_index + 1]:
            d[v-1] = min(d[v-1], d[min_index] + w)
    return d, visited


def network_delay_time(times: List[List[int]], N: int, K: int) -> int:
    nodemap = make_nodemap(times, N)
    lens_from_k, visited = dijkstra(nodemap, K, N)
    max_path = max(lens_from_k)
    if not all(visited) or (max_path == float('inf')):
        return -1
    else:
        return max_path
