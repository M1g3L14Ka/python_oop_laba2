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


class Programmer(Employee):
    def __init__(self, name, employee_id, programming_languages):
        super().__init__(name, employee_id)
        self.programming_languages = programming_languages

    def get_programming_languages(self):
        return self.programming_languages

    def code(self):
        return f"{self.name} is coding."


