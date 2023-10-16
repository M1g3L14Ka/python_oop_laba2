class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = float(salary)

    def display_name(self):
        return self.name

    def display_salary(self):
        return self.salary

    def upp_salary(self):
        self.salary *= 1.10


worker = Employee('misha', 35215.542)

print(f"Имя : {worker.display_name()}")
print(f"Зарплата : {worker.display_salary()}")

worker.upp_salary()
print(f"Увеличенная зарплата: {worker.display_salary()}")

