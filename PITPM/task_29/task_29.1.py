class User:
    name = "John"
    surname = "Smit"

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")


class Employee(User):
    pass


worker = Employee()
worker.display_info()
