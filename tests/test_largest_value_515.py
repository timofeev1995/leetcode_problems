import pytest
from problems.largest_value_in_each_tree_row_515.solution import largest_values, TreeNode


@pytest.mark.parametrize(
    ["tree", "expected"],
    [
        (
            TreeNode(
                1,
                TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3))
            ),
            [1, 2, 4]
        ),
        (
            TreeNode(
                1,
                TreeNode(10, None, TreeNode(4)),
                TreeNode(2, None, TreeNode(4))
            ),
            [1, 10, 4]
        ),
    ]
)
def test_largest_value(tree, expected):
    result = largest_values(tree)
    assert result == expected

