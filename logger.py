class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!


# Logger only logs interactions. To simulate a real outbreak, go to simulation.py or test it in its own file 
        # base_repo_rate = chace_to_infect
    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       base_repro_num):
        with open(self.file_name, 'w') as f:
            f.write(f"Metadata before the simulation starts:\n\n"
                    f"Population Size: {pop_size}\nVaccination Percentage: {vacc_percentage}\n"
                    f"Virus Name: {virus_name}\nMortality Rate: {mortality_rate}\n"
                    f"Basic Reproduction Number: {base_repro_num}\n"
                    f"{"-"*70}\n")

    def log_interactions(self, step_number, chance_to_infect, current_number_of_infected, new_infections, new_deaths):
        with open(self.file_name, 'a') as f:
            f.write(f"Current Step: {step_number}\n"
                    f"Chance to Infect: {chance_to_infect}\n"
                    f"New Infections This Step: {new_infections}\n"
                    f"Current Total Number of Infected: {current_number_of_infected}\n"
                    f"Number of Deaths This Step: {new_deaths}\n"
                    f"{"-"*70}\n")
            
    def log_infection_survival(self, total_number_of_interactions, total_vaccinated, total_dead):
        with open(self.file_name, 'a') as f:
            f.write(f"Total Interactions: {total_number_of_interactions}\n"
                    f"Total Vaccinated: {total_vaccinated}\n"
                    f"Total Dead: {total_dead}\n"
                    f"{"-"*70}\n")
# """
#     # Not used
#     def log_time_step(self, time_step_number):
#         pass        
# """   