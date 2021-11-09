from typing import List, Set, Mapping


def make_nodemap(prerequisites, num_courses):
    nodemap = {i: set() for i in range(num_courses)}
    for from_, to_ in prerequisites:
        nodemap[from_].add(to_)

    return nodemap


def has_cycle(nodemap, node, visited, current_visited):
    if node in visited:
        if node in current_visited:
            return True
        # Very important return:
        return False

    current_visited.add(node)
    visited.add(node)
    for c in nodemap[node]:
        if has_cycle(nodemap, c, visited, current_visited):
            return True

    current_visited.remove(node)
    return False


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    nodemap: Mapping[int, Set] = make_nodemap(prerequisites, num_courses)
    visited = set()
    for node in range(num_courses):
        if has_cycle(nodemap, node, visited, set()):
            return False
        visited.add(node)
    return True
