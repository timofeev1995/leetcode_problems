import pytest
from problems.network_delay_time_743.solution import network_delay_time


@pytest.mark.parametrize(
    ['times', 'N', 'K', 'expected'],
    [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1], [2, 1, 3]], 2, 2, 3),
        ([[1, 2, 1]], 2, 2, -1)
    ]
)
def test_network_delay_time(times, N, K, expected):
    result = network_delay_time(times, N, K)
    assert result == expected
