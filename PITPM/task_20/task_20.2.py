class Employee:
    __name = None

    def __init__(self, name):
        self.__name = name


emp1 = Employee('john')  # весь код, это одно большое задание,
emp2 = Employee('eric')  # которое выражается в сравнение имен

print(emp1 == emp2)

emp3 = Employee('john')
emp4 = Employee('eric')

print(emp3 == emp3)

emp5 = Employee('john')
emp6 = Employee('john')

print(emp5 == emp6)
