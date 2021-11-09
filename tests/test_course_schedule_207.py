import pytest
from problems.course_schedule_207.solution import can_finish


@pytest.mark.parametrize(
    ['num_courses', "prerequisites", "expected"],
    [
        (2, [[1, 0]], True),
        (2, [[0, 1]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[0, 1], [0, 2], [1, 2]], True)
    ]
)
def test_schedule(num_courses, prerequisites, expected):
    result = can_finish(num_courses, prerequisites)
    assert result == expected

