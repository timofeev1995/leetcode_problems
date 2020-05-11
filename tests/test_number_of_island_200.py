import pytest
from problems.number_of_island_200.solution import num_islands


@pytest.mark.parametrize(
    ["grid", 'expected'],
    [
        (
                [
                    ['1', '1', '1', '1', '0'],
                    ['1', '1', '0', '1', '0'],
                    ['1', '1', '0', '0', '0'],
                    ['0', '0', '0', '0', '0']
                ],
                1
        ),
        (
                [
                    ['1', '1', '0', '0', '0'],
                    ['1', '1', '0', '0', '0'],
                    ['0', '0', '1', '0', '0'],
                    ['0', '0', '0', '1', '1']
                ],
                3
        ),
    ]
)
def test_number_of_island(grid, expected):
    result = num_islands(grid)
    assert result == expected