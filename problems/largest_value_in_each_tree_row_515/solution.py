from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(accum: List[TreeNode]) -> List[int]:
    max_value = [max([x.val for x in accum if x])]
    new_accum = []
    for x in accum:
        if x:
            new_accum.append(x.left)
            new_accum.append(x.right)

    if any(new_accum):
        max_value.extend(bfs(new_accum))

    return max_value


def largest_values(root: TreeNode) -> List[int]:
    if not root:
        return None
    max_values = bfs([root])
    return max_values


