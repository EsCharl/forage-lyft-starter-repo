import unittest

from Tire.Octoprime import Octoprime


class TestOctoprime(unittest.TestCase):
    
    def test_tire_should_be_serviced(self):
        tire = Octoprime()
        tire.tire_sensor = [1, 1, 1, 1]
        
        self.assertTrue(tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        tire = Octoprime()
        tire.tire_sensor = [.8, .8, .8, .8]
        
        self.assertFalse(tire.needs_service())
    
    def test_tire_should_be_serviced_exact_point_9(self):
        tire = Octoprime()
        tire.tire_sensor = [.9, .9, .9, .9]
        
        self.assertTrue(tire.needs_service())
