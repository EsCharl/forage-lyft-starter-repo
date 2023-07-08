from battery.SpindlerBattery import SpindlerBattery
from car import Car
from engine.sternman_engine import SternmanEngine


class Palindrome(Car):
    def __init__(self, current_date, last_service_date, warning_light_on):
        super().__init__(SpindlerBattery(last_service_date, current_date), SternmanEngine(warning_light_on))
