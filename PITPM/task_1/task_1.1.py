class Car:
    color = None  # цвет автомобиля
    fuel = None  # количество топлива
    weight = None  # вес
    stamp = None  # марка

    def go(self):
        # Команда ехать:
        pass

    def turn(self):
        # Команда поворачивать:
        pass

    def stop(self):
        # Команда остановиться:
        pass


myCar = Car()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.weight = 0.7
myCar.stamp = "audi"

myCar.go()
myCar.turn()
myCar.stop()
