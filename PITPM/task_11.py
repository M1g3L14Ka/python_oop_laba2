class User:
    def __init__(self, name, surname):
        print(name + ' ' + surname)


u = User('John', 'Smith')


class Employee:  #задание 1, передайте в конструктор класса Employee имя и зарплату работника.
    def __init__(self, name, salary):
        print(name + ' ' + salary)


worker = Employee('Misha', '4343$')
