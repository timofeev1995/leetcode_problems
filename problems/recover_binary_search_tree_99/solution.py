class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def _equal_trees(self, tree_a, tree_b):
        if tree_a.val == tree_b.val:
            if tree_a.left and tree_b.left:
                left_equal = self._equal_trees(tree_a.left, tree_b.left)
            else:
                return False
            if tree_a.right and tree_b.right:
                right_equal = self._equal_trees(tree_a.right, tree_b.right)
            else:
                return False
            return left_equal and right_equal

        else:
            return False

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        return self._equal_trees(self, other)


def check_node(root, previous, incorrect_1, incorrect_2):
    if previous is None:
        previous = root
    if root.val < previous.val:
        if incorrect_1:
            incorrect_2 = root
        else:
            incorrect_1 = previous
            incorrect_2 = root
    else:
        previous = root
    return root, previous, incorrect_1, incorrect_2


def get_incorrect(root: TreeNode, previous, incorrect_1=None, incorrect_2=None):

    if (not root.left) & (not root.right):
        root, previous, incorrect_1, incorrect_2 = check_node(root, previous, incorrect_1, incorrect_2)
        return incorrect_1, incorrect_2, previous

    if root.left:
        incorrect_1, incorrect_2, previous = get_incorrect(root.left, previous, incorrect_1, incorrect_2)

    root, previous, incorrect_1, incorrect_2 = check_node(root, previous, incorrect_1, incorrect_2)

    if root.right:
        incorrect_1, incorrect_2, previous = get_incorrect(root.right, previous, incorrect_1, incorrect_2)
    return incorrect_1, incorrect_2, previous


def recover_tree(root):
    incorrect_1, incorrect_2, previous = get_incorrect(root, None, None, None)
    incorrect_1.val, incorrect_2.val = incorrect_2.val, incorrect_1.val
