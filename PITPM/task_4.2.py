class Employee:

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def display_info(self):
        print(f"Имя сотрудника: {self.name}")
        print(f"Зарплата: {self.salary}")
        print(f"Возраст: {self.age}")


worker = Employee("John", "5643$", "25")
worker.display_info()
