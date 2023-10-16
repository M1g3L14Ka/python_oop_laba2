class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Employee(User):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def get_employee_id(self):
        return self.employee_id


