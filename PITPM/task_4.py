class Employee:  # задание 2, свойства классов
    name = None
    salary = None

    def name(self):
        name = None

    def salary(self):
        salary = None

    def display_info(self):  # задание 3, вывод на экран имени и зарплаты (свойств)
        print('The first worker is', name1, "\nand his solar is", salary1)
        print('The second worker is', name2, "\nand his solar is", salary2)


name1 = "Jon"
salary1 = "6000$"
                    #задание 1, создание обьектов класса
name2 = "Eric"
salary2 = "6300$"

workers = Employee()
workers.display_info()
