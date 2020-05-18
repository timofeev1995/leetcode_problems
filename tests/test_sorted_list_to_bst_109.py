import pytest
from problems.sorted_list_to_bst_109.solution import ListNode, TreeNode, sorted_list_to_bst


@pytest.mark.parametrize(
    ['head', 'expected'],
    [
        (
            ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9))))),
            TreeNode(
                0,
                TreeNode(-3, TreeNode(-10)),
                TreeNode(9, TreeNode(5))
            )
        )
    ]
)
def test_sorted_list_to_bst(head, expected):
    # TODO: test (__eq__ on tree) has to be fixed
    result = sorted_list_to_bst(head)
    assert result == expected

