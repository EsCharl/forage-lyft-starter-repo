from battery.NubbinBattery import NubbinBattery
from car import Car
from engine.capulet_engine import CapuletEngine


class Thovex(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(NubbinBattery(last_service_date, current_date), CapuletEngine(current_mileage, last_service_mileage))
