import pytest
from problems.swim_in_rising_water_778.solution import swim_in_water


@pytest.mark.parametrize(
    ['grid', 'expected'],
    [
        (
                [
                    [0, 1, 2, 3, 4],
                    [24, 23, 22, 21, 5],
                    [12, 13, 14, 15, 16],
                    [11, 17, 18, 19, 20],
                    [10, 9, 8, 7, 6]
                ],
                16
        )
    ]
)
def test_swim_in_rising_water(grid, expected):
    # TODO: really slow solution, time complexity is huge
    result = swim_in_water(grid)
    assert result == expected
