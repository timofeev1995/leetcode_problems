import pytest
from problems.employee_importance_690.solution import Employee, get_importance


@pytest.mark.parametrize(
    ["employees", "id_", "expected"],
    [
        (
            [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])],
            1,
            11
        ),
    ]
)
def test_get_importance(employees, id_, expected):
    result = get_importance(employees, id_)
    assert result == expected
