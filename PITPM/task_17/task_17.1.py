class User:
    __name = None
    __surname = None

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def setName(self, name):
        self.__name = name

    def setSurname(self, surname):
        self.__surname = surname


user = User('', '')

user.setName("Alice")
user.setSurname("Smith")

print(user.getName())
print(user.getSurname())


class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def Getname(self):
        return self.__name

    def Getsalary(self):
        return self.__salary

    def Getage(self):
        return self.__age

    def Setname(self, name):
        self.__name = name

    def Setsalary(self, salary):
        self.__salary = salary

    def Setage(self, age):
        self.__age = age


worker = Employee('', '', '')

worker.Setname('Misha')
worker.Setsalary('34343')
worker.Setage('18')

print("Имя:", worker.Getname(), "\nЗарплата:", worker.Getsalary(), "\nВозраст:", worker.Getage())
