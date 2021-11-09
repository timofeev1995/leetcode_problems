import pytest
from problems.all_nodes_distance_863.solution import TreeNode, all_nodes_distance


@pytest.mark.parametrize(
    ["tree", "target", "K", "expected"],
    [
        (
            TreeNode(
                1,
                TreeNode(2),
                TreeNode(3, TreeNode(4))
            ),
            2,
            2,
            [3]
        ),
        (
            TreeNode(1),
            1,
            3,
            []
        ),
        (
            TreeNode(
                val=0,
                left=TreeNode(
                    val=1,
                    left=None,
                    right=TreeNode(
                        val=2,
                        left=None,
                        right=TreeNode(
                            val=3,
                            left=None,
                            right=TreeNode(
                                val=4,
                                left=None,
                                right=None
                            )
                        )
                    )
                ),
                right=None
            ),
            3,
            0,
            [3]
        ),
    ]
)
def test_all_nodes_distance(tree, target, K, expected):
    result = all_nodes_distance(tree, target, K)
    assert set(result) == set(expected)

