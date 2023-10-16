class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.__addSign(self.salary)

    def __addSign(self, num):  # P.S в задание надо сделать метод addSign приватным и все
        return num + '$'








