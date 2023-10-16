class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class Student(User):
    def setName(self, name):
        if len(name) > 0:
            super().setName(name)  # метод родителя
        else:
            print('student name error')