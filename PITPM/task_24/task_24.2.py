class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return f"{self.__salary}$"


employees = [
    Employee('john', 11412),
    Employee('eric', 12313),
    Employee('kyle', 12231),
]
for employee in employees:
    print(f"Имя: {employee.getName()}, Зарплата: {employee.getSalary()}")

