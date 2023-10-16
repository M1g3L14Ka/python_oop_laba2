class User:
    def __init__(self, name, surname):
        print(name + ' ' + surname)


u = User('John', 'Smith')


class Employee:
    def __init__(self, name, salary):
        print(name + ' ' + salary)


worker = Employee('Misha', '4343$')
