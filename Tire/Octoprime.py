from Tire.Tire import Tire


class Octoprime(Tire):
    def __init__(self):
        self.tire_sensor = [0, 0, 0, 0]
        
    def needs_service(self):
        for i in self.tire_sensor:
            if i >= 0.9:
                return True
        return False
        