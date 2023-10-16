class User:
    name = "john"

    def show(self):
        return self.name


user = User()

print(user.name)


class Student:
    name = "maks"
    surname = "millton"

    def show(self):
        return self.name

    def show1(self):
        return self.surname


student = Student()

