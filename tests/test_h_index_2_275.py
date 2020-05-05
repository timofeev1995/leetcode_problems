import pytest
from problems.h_index_2_275.solution import h_index


@pytest.mark.parametrize(
    ["citations", 'expected'],
    [
        ([0, 1, 3, 5, 6], 3),
        ([0, 1, 4, 4, 5, 6], 4),
    ]
)
def test_h_index_2(citations, expected):
    result = h_index(citations)
    assert result == expected
