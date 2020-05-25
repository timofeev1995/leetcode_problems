

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def is_leaf(node: TreeNode) -> bool:
    if not node.left and not node.right:
        return True
    else:
        return False


def dfs(tree: TreeNode) -> int:
    if is_leaf(tree):
        return 1

    left_depth = 0
    if tree.left:
        left_depth = dfs(tree.left)
    right_depth = 0
    if tree.right:
        right_depth = dfs(tree.right)

    return max(left_depth, right_depth) + 1


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return dfs(root)
