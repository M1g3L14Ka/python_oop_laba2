class Student:  # задание 1, создание класса и вписывание свойств
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_initials(self):  # задание 2, создание метода для отбора первого сивлоса с заглавной буквы
        initial_name = self.name[0].upper()
        initial_surname = self.surname[0].upper()
        return f"{initial_name}.{initial_surname}"


student = Student("zak", "milltone")  # задание 3, вывод символов
initials = student.get_initials()
print(initials)
