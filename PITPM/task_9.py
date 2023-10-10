class User:
    name = "john"

    def show(self):
        return self.name


user = User()

print(user.name)


class Student:  #задание 1, создать похожий класс
    name = "maks"  #задание 2, добавить в него name and surname
    surname = "millton"

    def show(self):
        return self.name

    def show1(self):
        return self.surname


student = Student()

print("Имя:", student.name)  #задание 3, вывести данные
print("Фамилия:", student.surname)
