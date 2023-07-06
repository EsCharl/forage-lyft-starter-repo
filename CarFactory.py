from car import Car
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(SpindlerBattery(last_service_date, current_date), CapuletEngine(current_mileage, last_service_mileage))
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(SpindlerBattery(last_service_date, current_date), WilloughbyEngine(current_mileage, last_service_mileage))
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        return Car(SpindlerBattery(last_service_date, current_date), SternmanEngine(warning_light_on))
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(NubbinBattery(last_service_date, current_date), WilloughbyEngine(current_mileage, last_service_mileage))
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(NubbinBattery(last_service_date, current_date), CapuletEngine(current_mileage, last_service_mileage))
    