import pytest

from problems.permutations_46.solution import permute


@pytest.mark.parametrize(
    ['nums', 'expected'],
    [
        (
            [1, 2, 3],
             [
                 [1, 2, 3],
                 [1, 3, 2],
                 [2, 1, 3],
                 [2, 3, 1],
                 [3, 1, 2],
                 [3, 2, 1]
             ]
         ),
    ]
)
def test_permutations(nums, expected):
    result = permute(nums)
    assert sorted(result) == sorted(expected)

