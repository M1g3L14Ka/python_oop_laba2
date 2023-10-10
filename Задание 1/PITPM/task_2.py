class Employee:  # задание 1, создание класса
    name = None
    age = None

    def name(self):
        name = None

    def age(self):
        age = None

    def display_info(self):  # задание 2, вывод информации о классе
        print(f"имя: {self.name}")
        print(f"возраст: {self.age}")


user = Employee()

user.name = "Света"
user.age = 35

user.display_info()  # вывод обьекта
