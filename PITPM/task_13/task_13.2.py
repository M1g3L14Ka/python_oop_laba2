class User:
    __name = None

    def __init__(self,name):
        self.__name = name

    def show(self):
        return self.__name


user = User('john')
print(user.show())


class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def show(self):
        return f'Имя {self.__name}, Зарплата {self.__salary} руб., Возраст {self.__age} лет'


worker = Employee('misha', 24142, 18)
print(worker.show())
