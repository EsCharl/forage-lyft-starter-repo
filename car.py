from GenerateRandomTire import generate_tire
from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, battery, engine, tire=generate_tire()):
        self.battery = battery
        self.engine = engine
        self.tire = tire
    
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
