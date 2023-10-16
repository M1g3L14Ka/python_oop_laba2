class Employee:
    def show(self, name, salary):
        return name + '' + salary + ''

    def display_info(self):  # первая версия вывода информации
        name = 'john'
        salary = ' 6500$'
        print(self.show(name, salary))


worker = Employee()
worker.display_info()

print(worker.show('mark ', '5400$'))  # вторая версия вывода информации