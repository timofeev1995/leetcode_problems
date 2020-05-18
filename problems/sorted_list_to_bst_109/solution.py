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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def count_len_of_list(head):
    if not head:
        return 0

    len_ = 1
    while True:
        head = head.next
        if head:
            len_ += 1
        else:
            break

    return len_


def build_tree(n, head) -> TreeNode:
    if n == 0:
        return None, head
    else:
        left_nodes, head = build_tree(n // 2, head)
        root_val = head.val
        head = head.next
        right_nodes, head = build_tree(n - (n // 2) - 1, head)
    return TreeNode(root_val, left_nodes, right_nodes), head


def sorted_list_to_bst(head: ListNode) -> TreeNode:
    list_len = count_len_of_list(head)
    tree, _ = build_tree(list_len, head)
    return tree
