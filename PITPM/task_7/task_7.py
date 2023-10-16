class Users:
    name = None

    def show(self):
        print(self.name)

user = Users()

user.name = "john"

user.show()


class Employee:  #задание 1, создание класса со свойствами
    name = None
    salary = None

    def name(self):
        name = None

    def salary(self):
        salary = None

    def display_info(self):  #задание 2, вывод информации
        print(f"имя: {self.name}")
        print(f"зарплата: {self.salary}")


worker = Employee()

worker.name = "misha"
worker.salary = "23000 руб."

worker.display_info()


class Employee1:  #вторая версия выполнения задания
    name = None
    salary = None

    def name_salary(self):
        print(f"имя: {self.name}" + f"\nзарплата: {self.salary}")


worker1 = Employee1()

worker1.name = 'milli'
worker1.salary = '4334$'

worker1.name_salary()
