class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 150  # Пример количества лошадиных сил


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "легковой автомобиль"
        self.price = 1500000  # Переопределение свойства price

    def horse_powers(self):
        return 200  # Переопределение функции horse_powers


nissan_car = Nissan()
print(nissan_car.vehicle_type, nissan_car.price)
