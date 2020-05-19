import pytest
from problems.binary_tree_inorder_traversal_94.solution import TreeNode, inorder_traversal


@pytest.mark.parametrize(
    ["tree", "expected"],
    [
        (
            TreeNode(
                1,
                TreeNode(-10),
                TreeNode(2, TreeNode(3))
            ),
            [-10, 1, 3, 2]
        ),
    ]
)
def test_inorder_traversal(tree, expected):
    result = inorder_traversal(tree)
    assert result == expected

