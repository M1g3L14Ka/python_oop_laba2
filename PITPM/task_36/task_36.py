class User:
    __age = 0

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age


class Student(User):
    __age = 0

    def __init__(self):
        __age = self.getAge()

    def defincAge(self):
        self.__age = self.__age + 1
