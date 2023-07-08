from battery.SpindlerBattery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine


class Calliope(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(SpindlerBattery(last_service_date, current_date), CapuletEngine(current_mileage, last_service_mileage))
