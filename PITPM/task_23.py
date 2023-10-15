class Position:
    def __init__(self, title):
        self.title = title


class Department:
    def __init__(self, name):
        self.name = name


class User:
    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department


position = Position("программист")
department = Department("Разработки")

employee = User("Михаил", position, department)

print("Имя:", employee.name)
print("Должность:", employee.position.title)
print("Отдел:", employee.department.name)
