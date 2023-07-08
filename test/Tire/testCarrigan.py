import unittest

from Tire.Carrigan import Carrigan


class TestCarrigan(unittest.TestCase):
    
    def test_tire_should_be_serviced(self):
        tire = Carrigan()
        tire.tire_sensor = [1, 1, 1, 1]
        
        self.assertTrue(tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        tire = Carrigan()
        tire.tire_sensor = [0, 0, 1, 1]
        
        self.assertFalse(tire.needs_service())
    
    def test_tire_should_be_serviced_exact_3(self):
        tire = Carrigan()
        tire.tire_sensor = [1, 1, 1, 0]
        
        self.assertTrue(tire.needs_service())
        