class Employee:
    def show(self):  # задание 1, создание и вызов текстового метода
        return "jsOpBsCM" # текст взят с git, а не придуман в ручную

    def display_info(self):
        print(f"текст: {self.show()}")

text = Employee()

text.display_info()
