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
myCar.go()
myCar.turn()
myCar.stop()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.weight = 0.7
myCar.stamp = "audi"

print(f"Цвет:", myCar.color)
print(f"Обьем бака:", myCar.fuel)
print(f"Вес:", myCar.weight)
print(f"Марка:", myCar.stamp)
