import random, math
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id: int, is_vaccinated: bool, infection = None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True


    def did_survive_infection(self):
        if self.infection is not None:
            immunity_rate = random.random()
            
            if immunity_rate > self.infection.mortality_rate:
                self.is_alive = True
                self.is_vaccinated = True
                self.infection = None
                return True
            else:
                self.alive = False
                return False