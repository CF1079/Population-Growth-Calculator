""" 
    popmod.py 
    -------------
    This version of code has been updated from the specialist maths 2021 IA1 Assignment
    It is still implementing a leslie matrix based approach, however, the key difference 
    is the code is written in an object oriented formated, ultimatley making the code more 
    efficient and easier to use. 
    A class is created called human. Whilst it may not be nessecary to use a single class in this script,
    this class will be copied and implemented in a greater heiarchy, where many species are created and modelled. 
    
"""

__date_created__ = '11/06/2023'
__last_update__ = '11/06/2023'

__author__ = 'Charlie Falk'
__version__ = '0.01' 
__date__ = '11/06/2023'

# dependencies 

import numpy as np
from time import sleep
from numpy.linalg import matrix_power
from matplotlib import pyplot as plt
from art import *
from popdb import PopDB

class Human:

    """
    Methods 
    -------
    simulate_growth -> function which calculates the population based on tuples it is given 
    
    """
   
    def __init__(self, popdb: object): 
        
        self._popdb = popdb 
        self._num_age_groups = self._popdb.get_number_age_groups()


    def simulate_growth(self, gens: int, high_series: tuple, medium_series: tuple, low_series: tuple): 
        """
        
        Parameters: 
        ----------

        gens: int -> how many generations will this predict

        high_series: tuple -> user inputs a tuple of the high series variable growth factors (float) in this format: 
            (<fertility_factor: float>, <survival_factor: float>, <NIM_factor: float>, <NOM_factor: float>)
        
        medium_series: tuple -> as per above

        low_series: tuple -> as per above 
        
        
        """

        # store data from csv 
        initial_populations = np.array([]) 
        survival_rates = np.array([]) 
        birth_rates = np.array([]) 
        net_interstate_migration = np.array([])
        net_overseas_migration = np.array([])
       
       # collect data
        for index in range(self._num_age_groups):
            initial_populations = np.append(initial_populations, self._popdb.get_pop_data(index, ['initial_population']))
            survival_rates = np.append(survival_rates, self._popdb.get_pop_data(index, ['survival_rate']))
            birth_rates = np.append(birth_rates, self._popdb.get_pop_data(index, ['birth_rate']))
            net_interstate_migration = np.append(net_interstate_migration, self._popdb.get_pop_data(index, ['net_interstate_migration']))
            net_overseas_migration = np.append(net_overseas_migration, self._popdb.get_pop_data(index, ['net_overseas_migration']))


        # format data 
        initial_populations = initial_populations.reshape(self._num_age_groups,1)
        survival_rates = survival_rates[0:-1]
        net_immigration_total = (net_interstate_migration + net_overseas_migration).reshape(self._num_age_groups, 1)
        initial_populations_immigration = (initial_populations + net_immigration_total)
        

        # create leslie matrix from this data 
        leslie_matrix = np.zeros((self._num_age_groups - 1, self._num_age_groups - 1))
        leslie_matrix[np.diag_indices_from(leslie_matrix)] = survival_rates
        leslie_matrix = np.append(leslie_matrix, np.zeros((self._num_age_groups-1,1)), axis=1)
        leslie_matrix = np.vstack([birth_rates, leslie_matrix])
        
        rows, cols = leslie_matrix.shape

        h_leslie_matrix = leslie_matrix.copy()
        m_leslie_matrix = leslie_matrix.copy()
        l_leslie_matrix = leslie_matrix.copy()

        # collect 'dynamic factors' and assign to variable 
        H_FERTILITY_FACTOR = high_series[0]; 
        H_SURVIVAL_FACTOR = high_series[1]
        H_IMMMIGRATION_FACTOR = high_series[2] + high_series[3]

        M_FERTILITY_FACTOR = medium_series[0]
        M_SURVIVAL_FACTOR = medium_series[1]
        M_IMMMIGRATION_FACTOR = medium_series[2] + medium_series[3]

        L_FERTILITY_FACTOR = low_series[0]
        L_SURVIVAL_FACTOR = low_series[1]
        L_IMMMIGRATION_FACTOR = low_series[2] + low_series[3]
    

        # create a leslie matrix for every 'gen'
        # create one for high, medium and low series 
        hseries_nat_leslies = []
        mseries_nat_leslies = []
        lseries_nat_leslies = []

        # for every leslie matrix update the fertility rates, as a function of time 
        for gen in range(1,gens + 1): 
            #update matrix values with growth factors as a linear function considering time 
            for row in range(rows): 
                birthrate = leslie_matrix[0][row]
                if birthrate > 0:
                    h_leslie_matrix[0][row] += H_FERTILITY_FACTOR 
                    m_leslie_matrix[0][row] += M_FERTILITY_FACTOR 
                    l_leslie_matrix[0][row] += L_FERTILITY_FACTOR 
                else: 
                    pass 
            
            # simily, update the survival rates as a function of time 
            for col in range(cols-1): 
                column = leslie_matrix[:,col]
                survivalrate = column[col+1]
                if survivalrate > 0: 
                     h_leslie_matrix[col+1][col] += H_SURVIVAL_FACTOR
                     m_leslie_matrix[col+1][col] += M_SURVIVAL_FACTOR
                     l_leslie_matrix[col+1][col] += L_SURVIVAL_FACTOR
                else: 
                    pass 
           
           # raise the matrix to power 'gen' and store in a list 
            hseries_nat_leslies.append(np.linalg.matrix_power(h_leslie_matrix, gen))  
            mseries_nat_leslies.append(np.linalg.matrix_power(m_leslie_matrix, gen))  
            lseries_nat_leslies.append(np.linalg.matrix_power(l_leslie_matrix, gen))  
        
        # multiple every leslie matrix by the iniital population matrix 
        h_natincr_matrx = []
        for leslie in hseries_nat_leslies:
            h_natincr_matrx.append(np.matmul(leslie, initial_populations))
        
        m_natincr_matrx = []
        for leslie in mseries_nat_leslies:
            m_natincr_matrx.append(np.matmul(leslie, initial_populations))
        
        l_natincr_matrx = []
        for leslie in lseries_nat_leslies:
            l_natincr_matrx.append(np.matmul(leslie, initial_populations))

        # sum every population solution to get a single value, for every value of the generation
        # ie at gen 40, population is .....
        h_natincr_sum = []
        for pop_mat in h_natincr_matrx: 
            h_natincr_sum.append(np.sum(pop_mat))
        
        m_natincr_sum = []
        for pop_mat in m_natincr_matrx: 
            m_natincr_sum.append(np.sum(pop_mat))
        
        l_natincr_sum = []
        for pop_mat in l_natincr_matrx: 
            l_natincr_sum.append(np.sum(pop_mat))

        # create initial population matricies including immigration 
        h_intpop_immigration = initial_populations_immigration.copy()
        m_intpop_immigration = initial_populations_immigration.copy()
        l_intpop_immigration = initial_populations_immigration.copy()
        
        # update population matrix with immigration factor for every gen
        h_immigration_intpop = []
        m_immigration_intpop = []
        l_immigration_intpop = []
        for gen in range(1, gens+1):
            h_intpop_immigration += H_IMMMIGRATION_FACTOR
            h_immigration_intpop.append(np.copy(h_intpop_immigration))
            m_intpop_immigration += M_IMMMIGRATION_FACTOR
            m_immigration_intpop.append(np.copy(m_intpop_immigration))
            l_intpop_immigration += L_IMMMIGRATION_FACTOR
            l_immigration_intpop.append(np.copy(l_intpop_immigration))

        # multiply immigration leslie x immigration population matrix 
        h_immigration_pop = np.matmul(hseries_nat_leslies, h_immigration_intpop)
        m_immigration_pop = np.matmul(mseries_nat_leslies, m_immigration_intpop) 
        l_immigration_pop = np.matmul(lseries_nat_leslies, l_immigration_intpop) 

        # sum solution matrix for a single value
        h_immigration_sum = []
        for pop_mat in h_immigration_pop:
            h_immigration_sum.append(np.sum(pop_mat))
        
        m_immigration_sum = []
        for pop_mat in m_immigration_pop:
            m_immigration_sum.append(np.sum(pop_mat))
        
        l_immigration_sum = []
        for pop_mat in l_immigration_pop:
            l_immigration_sum.append(np.sum(pop_mat))
        
        # plot the data 
        x_data = np.linspace(0, gens, gens)
        fig, ax = plt.subplots()
        ax.plot(x_data, h_immigration_sum, label='High Series Immigration Increase')
        ax.plot(x_data, h_natincr_sum,label='High Series Natural Increase')
        ax.plot(x_data, m_immigration_sum, label='Medium Series Immigration Increase')
        ax.plot(x_data, m_natincr_sum,label='Medium Series Natural Increase')
        ax.plot(x_data, l_immigration_sum, label='Low Series Immigration Increase')
        ax.plot(x_data, l_natincr_sum,label='Low Series Natural Increase')
        plt.xlabel('Number Generations')
        plt.ylabel('Number People')
        ax.set_title('Population Growth')
        ax.grid(True)
        ax.legend( loc='best')
        plt.show()

def main(): 
    tprint("\nPopulation Growth Calculator!")
    print("************************************************************************************************")
    print("\n Copyright © of Charlie Falk, 2023")
    print("\n Built for the IA1 Specialists Maths PSMT")
    print("\n 40-year Projection of the Population of Victoria")
    print("\n************************************************************************************************")
    sleep(1)
    print("\n\n\n\nGenerating Plot.......")
    sleep(2)
    print("\n\n\n\nExit Graph to Quit\n\n")
    sleep(0.5)
    popdb = PopDB('test_database.csv')
    popsim = Human(popdb)
    high_series = (0.000011815,0.0000254545, 1180.0, 7588.0) # enter 'dynamic factors' for high, medium and low series 
    med_series = (0, 0, -440.0, -1455.0) # leave these as 0 if you wish to have no dynamic factors, they are preset to what I used for the assignment, that is set for victoria up to 40 years (from 2021). 
    low_series = (-0.0000281844, -0.0000145455, -1276.0, -3936.0)
    popsim.simulate_growth(40,high_series, med_series, low_series) # this model is valid up to 40 gens 
    sleep(0.5)
    print("\n\n\nGoodbye\n\n\n")


main()