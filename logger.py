class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
        
    def write_metadata(self, pop_size, vacc_percentage, virus, initial_infected):
        with open(self.file_name, 'w') as f:
            f.write(f"Metadata before the simulation starts:\n\n"
                    f"Population Size: {pop_size}\n"
                    f"Vaccination Percentage: {vacc_percentage}\n"
                    f"Virus Name: {virus.name}\n"
                    f"Initial Infected: {initial_infected}\n"
                    f"{"-"*70}\n")

    def log_interactions(self, step_number, number_of_interactions, dead_people, total_vaccinated, total_infections):
        with open(self.file_name, 'a') as f:
            f.write(f"Current Step: {step_number}\n"
                    f"Number of interactions: {number_of_interactions}\n"
                    f"Dead People: {dead_people}\n"
                    f"Total Vaccinated: {total_vaccinated}\n"
                    f"Total Infections Remaining in This Step: {total_infections}\n"
                    f"{"-"*70}\n")
            
    def log_infection_survival(self, step_number, number_of_interactions, dead_people, total_vaccinated, total_infections, virus, pop_size, initial_infected, vacc_percentage):
        with open(self.file_name, 'a') as f:
            f.write(f"Step: {step_number}\n"
                    f"Number of interactions: {number_of_interactions}\n"
                    f"Dead People: {dead_people}\n"
                    f"Total Vaccinated: {total_vaccinated}\n"
                    f"Total Infections: {total_infections}\n"
                    f"Virus: {virus.name}\n"
                    f"Population Size: {pop_size}\n"
                    f"Initial Infected: {initial_infected}\n"
                    f"Vaccination Percentage: {vacc_percentage}\n"
                    f"{"-"*70}\n")
            
    def test(self, option):
        with open(self.file_name, 'a') as f:
            f.write(f"{option}")
# """
#     # Not used
#     def log_time_step(self, time_step_number):
#         pass        
# """   