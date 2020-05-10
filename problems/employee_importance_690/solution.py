from typing import List, Set


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

    def __repr__(self):
        return str(self.id)


def make_dict(employees):
    memory = {}
    for e in employees:
        memory.update({e.id: e})
    return memory


def dfs(employees, employee_id: int):
    current_employee = employees[employee_id]
    if len(current_employee.subordinates) == 0:
        return current_employee.importance
    else:
        importance = []
        for sub in current_employee.subordinates:
            child_importance = dfs(employees, sub)
            importance.append(child_importance)
        return sum(importance) + current_employee.importance


def get_importance(employees: List[Employee], id_: int) -> int:
    employees_dict = make_dict(employees)
    importance = dfs(employees_dict, id_)
    return importance