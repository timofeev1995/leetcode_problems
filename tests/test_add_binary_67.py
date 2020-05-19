import pytest
from problems.add_binary_67.solution import add_binary


@pytest.mark.parametrize(
    ["a", "b", 'expected'],
    [
        ("11", "1", "100"),
        ("1010", "1011", "10101")
    ]
)
def test_add_binary(a, b, expected):
    result = add_binary(a, b)
    assert result == expected

