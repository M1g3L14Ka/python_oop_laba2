class Employee:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Возраст: {self.age}")


worker = Employee("James", "Bond", 42)
worker.display_info()
