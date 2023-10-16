class Student:  
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_initials(self):
        initial_name = self.name[0].upper()
        initial_surname = self.surname[0].upper()
        return f"{initial_name}.{initial_surname}"


student = Student("zak", "milltone")
initials = student.get_initials()
print(initials)
