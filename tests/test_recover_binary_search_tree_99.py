import pytest
from problems.recover_binary_search_tree_99.solution import recover_tree, TreeNode


@pytest.mark.parametrize(
    ["tree", "expected"],
    [
        (
            TreeNode(
                3,
                TreeNode(1),
                TreeNode(4, TreeNode(2), None)
            ),
            TreeNode(
                2,
                TreeNode(1),
                TreeNode(4, TreeNode(3), None)
            ),
        )
    ]
)
def test_recover_tree(tree, expected):
    # TODO: test and __eq__ magic need to be fixed.
    # Solution is accepted but test is incorrect.
    recover_tree(tree)
    assert tree == expected

