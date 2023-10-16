class user:
    name = None


user.name = 'john'
user.surname = 'smit'
print(user.name)
print(user.surname)

print("=============================")  # разделение

class Employee:  #задание 1, добавть к классу свойства
    name = None
    age = None
    salary = None

    def name(self):
        name = None

    def age(self):
        age = None

    def salary(self):
        salary = None

    def display_info(self):  #задание 2, получение данных и вывод их
        print(f"имя: {self.name}")
        print(f"возраст: {self.age}")
        print(f"зарплата: {self.salary}")


users = Employee()
users.name = "Вика"
users.age = 24
users.salary = 35000

users.display_info()
