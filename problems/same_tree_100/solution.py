class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(tree):

    if not tree:
        return -1

    nodes = [tree.val]
    if tree.left:
        nodes.extend(dfs(tree.left))
    else:
        nodes.append(None)
    if tree.right:
        nodes.extend(dfs(tree.right))
    else:
        nodes.append(None)

    return nodes


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """

    :param p: `TreeNode`
    :param q: `TreeNode`
    :return: `bool` are p == q
    """
    return dfs(q) == dfs(p)