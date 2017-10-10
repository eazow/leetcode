class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employees_map = {}
        for employee in employees:
            employees_map[employee.id] = employee

        importance_map = {}
        def get_importance(id):
            employee = employees_map.get(id)
            subordinates = employee.subordinates
            importance = employee.importance
            for subordinate in subordinates:
                if not importance_map.get(subordinate):
                    importance_map[subordinate] = get_importance(subordinate)
                importance += importance_map.get(subordinate)

            return importance

        return get_importance(id)

employee1 = Employee(1, 5, [2, 3])
employee2 = Employee(2, 3, [])
employee3 = Employee(3, 3, [])
assert Solution().getImportance([employee1, employee2, employee3], 1) == 11