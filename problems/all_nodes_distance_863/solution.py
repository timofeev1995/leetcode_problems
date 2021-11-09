from typing import List, Dict, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def update_accumulator(accumulator, node_a, node_b):
    if node_a not in accumulator:
        accumulator[node_a] = {node_b}
    else:
        accumulator[node_a].add(node_b)


def dfs(tree: TreeNode, accumulator: Dict[int, Set[int]]):
    parent_id = tree.val
    if tree.left is not None:
        update_accumulator(accumulator, parent_id, tree.left.val)
        update_accumulator(accumulator, tree.left.val, parent_id)
        dfs(tree.left, accumulator)
    if tree.right is not None:
        update_accumulator(accumulator, parent_id, tree.right.val)
        update_accumulator(accumulator, tree.right.val, parent_id)
        dfs(tree.right, accumulator)


def bfs(graph, node, k):
    result_nodes = set()
    neighbors = graph[node]
    if k == 1:
        return neighbors
    for n in neighbors:
        _ = graph[n].remove(node)
        result_nodes.update(bfs(graph, n, k-1))

    return result_nodes


def get_graph(root: TreeNode) -> Dict[int, Set[int]]:
    node_neighbors = {}
    dfs(root, node_neighbors)
    return node_neighbors


def get_k_distance_neighbors(graph, target, K):
    result_nodes = bfs(graph, target, K)
    return result_nodes


def all_nodes_distance(root: TreeNode, target: TreeNode, K: int) -> List:
    graph = get_graph(root)
    if len(graph) == 0:
        return []
    if K == 0:
        return [target]
    result = get_k_distance_neighbors(graph, target, K)
    return result



