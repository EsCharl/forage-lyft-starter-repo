import unittest
from datetime import datetime

from battery.SpindlerBattery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    
    def test_battery_should_be_serviced(self):
        last_service_date = datetime.now().replace(year=datetime.now().year - 3)
        battery = SpindlerBattery(last_service_date)
        
        self.assertTrue(battery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        last_service_date = datetime.now().replace(year=datetime.now().year - 1)
        battery = SpindlerBattery(last_service_date)
        
        self.assertFalse(battery.needs_service())
    
    def test_battery_should_not_be_serviced_on_year(self):
        last_service_date = datetime.now().replace(year=datetime.now().year - 2)
        battery = SpindlerBattery(last_service_date)
        
        self.assertFalse(battery.needs_service())
