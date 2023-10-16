class User:
    __name = None
    __surname = None

    def getName(self):
        return self.__name

    def getSurn(self):
        return self.__surname

    def setName(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            raise Exception('name is incorrect')

    def setSurn(self, surname):
        if len(surname) > 0:
            self.__surname = surname
        else:
            raise Exception("surname is incorrect!")


user = User()
user.setName('john')


class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def Getname(self):
        return self.__name

    def Getsalary(self):
        return f"{self.__salary}$"

    def Getage(self):
        return self.__age

    def Setage(self, age):
        if age < 0:
            print("Age must be between 0 and 120.")
        else:
            self.__age = age

        if age > 120:
            print("Age must be between 0 and 120.")
        else:
            self.__age = age


worker = Employee('Misha', 4636, 26)
print("Имя:", worker.Getname())
print("Зарплата:", worker.Getsalary())
print("Возраст:", worker.Getage())
