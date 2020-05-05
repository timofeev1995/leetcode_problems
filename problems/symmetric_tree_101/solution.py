from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_flatten_node_list(root: TreeNode, mode: str = 'left') -> List:

    accum = [root.val]
    mode_opposite = 'right' if mode == 'left' else 'left'

    mode_root = getattr(root, mode)
    if mode_root:
        mode_nodes = get_flatten_node_list(mode_root, mode)
    else:
        mode_nodes = [None]

    mode_opposite_root = getattr(root, mode_opposite)
    if mode_opposite_root:
        mode_opposite_nodes = get_flatten_node_list(mode_opposite_root, mode)
    else:
        mode_opposite_nodes = [None]

    accum.extend(mode_nodes)
    accum.extend(mode_opposite_nodes)

    return accum


def is_symmetric(root: TreeNode) -> bool:
    """

    :param root: `TreeNode` binary tree:
                    1
                   / \
                  2   2
                 / \ / \
                3  4 4  3
    :return: True/False is a `Tree` root symmetric.
    """
    if not root:
        return True
    # If we dont have right-left children - symmetric
    elif (not root.left) and (not root.right):
        return True
    # If we have only left/right - non symmetric
    elif (not root.left) or (not root.right):
        return False
    # Else we will descent tree for left branch left-to-right
    # and right-to-left for right branch.
    # So if collected nodes are equal its symmetric.
    else:
        left_flatten = get_flatten_node_list(root.left, 'left')
        right_flatten = get_flatten_node_list(root.right, 'right')
        if left_flatten == right_flatten:
            return True
        else:
            return False

