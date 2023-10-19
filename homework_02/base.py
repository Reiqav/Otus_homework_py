"""
- доработайте базовый класс `base.Vehicle`:
    - добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
    - добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`
    - добавьте метод `start`. При вызове этого метода необходимо проверить состояние `started`. И если не `started`, то нужно проверить, что топлива больше нуля, 
      и обновить состояние `started`, иначе нужно выкинуть исключение `exceptions.LowFuelError`
    - добавьте метод `move`, который проверяет, 
      что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), 
      и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
"""

from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=1000, fuel=100, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.fuel > 0 and self.started is False:
            self.started = True
        elif self.started is True:
            print(f'Started is True')
        else:
            raise LowFuelError(f'Low Fuel')

    def move(self, distance):
        if 0 <= self.fuel <= self.fuel_consumption:
            raise NotEnoughFuel('Not Fuel')
        elif self.fuel < (distance * self.fuel_consumption):
            raise NotEnoughFuel('Not Fuel')
        else:
            self.fuel -= (distance * self.fuel_consumption)
