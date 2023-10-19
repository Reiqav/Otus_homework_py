"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, *args):
        self.message = None

    def __str__(self):
        if self.message:
            return 'LowFuelError'


class NotEnoughFuel(Exception):
    def __init__(self, *args):
        self.message = None

    def __str__(self):
        if self.message:
            return 'NotEnoughFuel'


class CargoOverload(Exception):
    def __init__(self, *args):
        self.message = None

    def __str__(self):
        if self.message:
            return 'CargoOverload'
