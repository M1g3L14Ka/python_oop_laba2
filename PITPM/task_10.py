class User:

    def __init__(self):
        print('+++')


user = User()


class Employee:  #задание 1, сделайте конструктор класса Employee, со свойствами из предыдущих примеров

    def __init__(self):
        self.name = "Sveta"
        self.surname = "Milanova"
        self.salary = "3252$"
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Зарплата: {self.salary}")


worker = Employee()
