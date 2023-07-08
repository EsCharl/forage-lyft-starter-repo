from datetime import datetime

from battery.NubbinBattery import NubbinBattery
from car import Car
from engine.willoughby_engine import WilloughbyEngine


class Rorschach(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(NubbinBattery(last_service_date, current_date), WilloughbyEngine(current_mileage, last_service_mileage))
