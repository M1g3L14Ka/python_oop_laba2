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

emp7 = Employee('john')
emp8 = Employee('eric')

print(emp7 != emp7)

emp9 = Employee('john')
emp10 = emp9

print(emp9 == emp10)

emp11 = Employee('john')
emp12 = Employee('eric')

print(emp11 != emp12)

emp13 = Employee('john')
emp14 = emp13
emp14.name = 'eric'

print(emp13 == emp14)
