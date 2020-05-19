from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def inorder_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []

    traversal = []
    stack = [(root, False)]
    while stack:
        node, add_flag = stack.pop()
        if node:
            if add_flag:
                traversal.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

    return traversal

