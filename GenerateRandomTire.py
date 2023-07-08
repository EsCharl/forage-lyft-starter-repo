import random

from Tire.Carrigan import Carrigan
from Tire.Octoprime import Octoprime


def generate_tire():
    if random.getrandbits(1):
        return Carrigan()
    return Octoprime()
