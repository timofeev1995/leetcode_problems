import pytest
from problems.number_complement_476.solution import find_complement


@pytest.mark.parametrize(
    ["num", 'expected'],
    [
        (5, 2),
        (1, 0),
        (0, 1)
    ]
)
def test_find_complements(num, expected):
    result = find_complement(num)
    assert result == expected
