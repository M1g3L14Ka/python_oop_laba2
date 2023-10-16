class User:
    name = None
    year = None


class Student(User):
    def Year(self, name, year):
        self.name = name
        self.year = year


student = Student()
student.name = "John"
student.year = "2023"

print(student.name, student.year)
