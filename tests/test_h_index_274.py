import pytest
from problems.h_index_274.solution import h_index


@pytest.mark.parametrize(
    ["citations", 'expected'],
    [
        ([0, 1, 3, 5, 6], 3),
        ([0, 1, 4, 4, 5, 6], 4),
        ([3, 0, 6, 1, 5], 3),
        ([0, 0], 0),
        ([11, 222], 2)
    ]
)
def test_h_index(citations, expected):
    result = h_index(citations)
    assert result == expected
