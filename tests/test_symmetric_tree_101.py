import pytest
from problems.symmetric_tree_101.solution import is_symmetric, TreeNode


@pytest.mark.parametrize(
    ["tree", "expected"],
    [
        (
            TreeNode(
                1,
                TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3))
            ),
            True
        ),
        (
            TreeNode(
                1,
                TreeNode(2, None, TreeNode(4)),
                TreeNode(2, None, TreeNode(4))
            ),
            False
        ),
    ]
)
def test_symmetric_tree(tree, expected):
    result = is_symmetric(tree)
    assert result == expected

