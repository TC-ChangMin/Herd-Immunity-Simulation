import random, math
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id: int, is_vaccinated: bool, infection_name = None):
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection_name = infection_name
        self.is_alive = True


    def did_survive_infection(self):
        if self.infection_name is not None:
            immunity_rate = round(random.uniform(0.0, 1.0), 2)
            
            # print(f"Immunity rate: {immunity_rate}")
            # print(f"Mortality rate: {self.infection_name.mortality_rate}")
            if immunity_rate <= self.infection_name.mortality_rate: # if randnum is less than the mortality rate, person is dead.
                self.is_alive = False
                return self.is_alive
            else:
                self.is_vaccinated = True
                self.is_alive = True
                return self.is_vaccinated, self.is_alive

if __name__ == "__main__":
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection_name is None


    unvaccinated_person = Person(2, False)
    # print(f"ID: {vaccinated_person._id}, Is vaccinated: {vaccinated_person.is_vaccinated}")
    # print(f"ID: {unvaccinated_person._id}, Is vaccinated: {unvaccinated_person.is_vaccinated}")

    # reads as follows: Virus(name, repro_rate, mortality_rate)
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values of each attribute
    # assert ...

    # infected_person.did_survive_infection()

    # print(f"ID: {infected_person._id}, Is vaccinated: {infected_person.is_vaccinated}, Infection: {infected_person.infection_name}, Is alive: {infected_person.is_alive}")

    people = []
    total_survived = 0
    total_dead = 0

    for i in range(1, 101):
        test_person = Person(i, False, virus)
        people.append(test_person)

    for person in people:
        survived = person.did_survive_infection()
        if survived:
            total_survived += 1
        else:
            total_dead += 1
        # print(f"ID: {person._id}, Is vaccinated: {person.is_vaccinated}, Infection: {person.infection_name}, Is alive: {person.is_alive}")
    print(f"Total Survived: {total_survived}, Total Dead: {total_dead}")

    
    # Count the people that survived and did not survive: 
   
    # did_survived = 0
    # did_not_survive = 0

    # TODO Loop over all of the people 
    # TODO If a person is_alive True add one to did_survive
    # TODO If a person is_alive False add one to did_not_survive

    # TODO When the loop is complete print your results.
    # The results should roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 rough 20% of the people 
    # should succumb. 

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 

    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.