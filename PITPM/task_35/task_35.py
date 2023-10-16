class User:
    __name = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Student(User):
    pass


student = Student()
student.setName('john')
name = student.getName()
print(name)