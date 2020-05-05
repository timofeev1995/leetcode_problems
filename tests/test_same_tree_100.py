import pytest
from problems.same_tree_100.solution import is_same_tree, TreeNode


@pytest.mark.parametrize(
    ['p', 'q', 'expected'],
    [
        (
            TreeNode(
                1,
                TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3))
            ),
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
                TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3))
            ),
            TreeNode(
                1,
                TreeNode(1213, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3))
            ),
            False
        )
    ]
)
def test_same_tree(p, q, expected):
    result = is_same_tree(p, q)
    assert result == expected

