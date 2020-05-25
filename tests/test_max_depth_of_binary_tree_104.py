import pytest
from problems.max_depth_of_binary_tree_104.solution import max_depth, TreeNode


@pytest.mark.parametrize(
    ["tree", "expected"],
    [
        (
            TreeNode(
                1,
                TreeNode(-10),
                TreeNode(2, TreeNode(3))
            ),
            3
        ),
    ]
)
def test_max_depth(tree, expected):
    result = max_depth(tree)
    assert result == expected

