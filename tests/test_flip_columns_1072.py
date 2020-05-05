import pytest
from problems.flip_columns_1072.solution import max_equal_rows_after_flips


@pytest.mark.parametrize(
    ['matrix', 'expected'],
    [
        ([[0,1],[1,1]], 1),
        ([[0,0,0],[0,0,1],[1,1,0]], 2)
    ]
)
def test_flip_columns(matrix, expected):
    result = max_equal_rows_after_flips(matrix)
    assert result == expected

