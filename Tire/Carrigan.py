from Tire.Tire import Tire


class Carrigan(Tire):
    def __init__(self):
        self.tire_sensor = [0, 0, 0, 0]
    
    def needs_service(self):
        if sum(self.tire_sensor) >= 3:
            return True
        else:
            return False
