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
        return f"{self.__name}, {self.__salary}, {self.__age}"

