import os
from logger import Logger

def test_write_metadata():
    file_name = 'simulation_test.txt'
    logger = Logger(file_name)
    
    pop_size = 1000
    vacc_percentage = 0.1
    virus_name = 'TestVirus'
    mortality_rate = 0.05
    # base_repro_num = 2.5
    
    logger.write_metadata(pop_size, vacc_percentage, virus_name, mortality_rate)
    
    x = 1
    end_step = int(input("Enter a number: "))
    while x < end_step+1:
        logger.log_interactions(x, "[Chance to Infect]", "[New Infections This Step]", "[Current Total Infected]", "[Deaths This Step]")
        x += 1
    # os.remove(file_name)

if __name__ == "__main__":
    test_write_metadata()
    # print("All tests passed.")