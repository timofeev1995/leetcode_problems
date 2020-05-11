import pytest
from problems.friend_circles_547.solution import find_circle_num


@pytest.mark.parametrize(
    ["matrix", 'expected'],
    [
        (
                [
                    [1, 1, 0],
                    [1, 1, 0],
                    [0, 0, 1]
                ],
                2
        ),
        (
                [
                    [1, 1, 0],
                    [1, 1, 1],
                    [0, 1, 1]
                ],
                1
        ),
    ]
)
def test_friend_circle(matrix, expected):
    result = find_circle_num(matrix)
    assert result == expected
