class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class Student(User):
    def setName(self, name):
        if len(name) > 0:
            self.name = name
        else:
            print("student name error")


student = Student()
student.setName('john')
student.setName('')  # ошибка
