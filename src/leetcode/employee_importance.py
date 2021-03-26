"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee = None
        
        for e in employees:
            if e.id == id:
                employee = e

        if employee is None:
            return 0
        
        res = employee.importance
        stack = [*employee.subordinates]
        visited = { employee.id }
        employee_ids_map = { emp_i.id:emp_i for emp_i in employees }
        
        while stack:
            e_id = stack.pop()
            
            if e_id in visited:
                continue
                
            e = employee_ids_map[e_id]                
            res += e.importance
                
            for sub_id in e.subordinates:
                stack.append(sub_id)
                
        return res
