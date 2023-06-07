""" 
    Population.py 
    -------------
    This version of code has been updated from the specialist maths 2021 IA1 Assignment
    It is still implementing a leslie matrix based approach, however, the key difference 
    is the code is written in an object oriented formated, ultimatley making the code more 
    efficient and easier to use. 
    
"""

## THIS WILL HAVE TO BE A GUI IN ORDER TO RUN AS A .exe or .dmg 

__date_created__ = '11/06/2023'
__last_update__ = '11/06/2023'

__author__ = 'Charlie Falk'
__version__ = '0.01' 
__date__ = '11/06/2023'



## dependencies 

import numpy as np
from time import sleep
from numpy.linalg import matrix_power
from matplotlib import pyplot as plt
from art import *
from popdb import PopDB


class Population: 
    """ 
    
    """
    pass 

class Human(Population):

    """
    Methods 
    -------

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

        initial_populations = np.array([]) # np.array containing all of the age groups initial population values 
        survival_rates = np.array([]) # list containing all of the age groups survival rates 
        birth_rates = np.array([]) # list containing all of the age groups birth rates 
        net_interstate_migration = np.array([])
        net_overseas_migration = np.array([])
       
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

        H_FERTILITY_FACTOR = high_series[0]; 
        H_SURVIVAL_FACTOR = high_series[1]
        H_IMMMIGRATION_FACTOR = high_series[2] + high_series[3]

        M_FERTILITY_FACTOR = medium_series[0]
        M_SURVIVAL_FACTOR = medium_series[1]
        M_IMMMIGRATION_FACTOR = medium_series[2] + medium_series[3]

        L_FERTILITY_FACTOR = low_series[0]
        L_SURVIVAL_FACTOR = low_series[1]
        L_IMMMIGRATION_FACTOR = low_series[2] + low_series[3]
    
        hseries_nat_leslies = []
        mseries_nat_leslies = []
        lseries_nat_leslies = []

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
           
            for col in range(cols-1): 
                column = leslie_matrix[:,col]
                survivalrate = column[col+1]
                if survivalrate > 0: 
                     h_leslie_matrix[col+1][col] += H_SURVIVAL_FACTOR
                     m_leslie_matrix[col+1][col] += M_SURVIVAL_FACTOR
                     l_leslie_matrix[col+1][col] += L_SURVIVAL_FACTOR
                else: 
                    pass 
           
            hseries_nat_leslies.append(np.linalg.matrix_power(h_leslie_matrix, gen))  
            mseries_nat_leslies.append(np.linalg.matrix_power(m_leslie_matrix, gen))  
            lseries_nat_leslies.append(np.linalg.matrix_power(l_leslie_matrix, gen))  
 
        ## Calculate each of the populations 

       ##################

        h_natincr_matrx = []
 
        for leslie in hseries_nat_leslies:
            h_natincr_matrx.append(np.matmul(leslie, initial_populations))
        
        m_natincr_matrx = []

        for leslie in mseries_nat_leslies:
            m_natincr_matrx.append(np.matmul(leslie, initial_populations))
        
        l_natincr_matrx = []

        for leslie in lseries_nat_leslies:
            l_natincr_matrx.append(np.matmul(leslie, initial_populations))
        
        ##################
        
        h_natincr_sum = []
        for pop_mat in h_natincr_matrx: 
            h_natincr_sum.append(np.sum(pop_mat))
        
        m_natincr_sum = []
        for pop_mat in m_natincr_matrx: 
            m_natincr_sum.append(np.sum(pop_mat))
        
        l_natincr_sum = []
        for pop_mat in l_natincr_matrx: 
            l_natincr_sum.append(np.sum(pop_mat))

        ###################
        
        h_intpop_immigration = initial_populations_immigration.copy()
        m_intpop_immigration = initial_populations_immigration.copy()
        l_intpop_immigration = initial_populations_immigration.copy()
        
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

        h_immigration_pop = np.matmul(hseries_nat_leslies, h_immigration_intpop)
        m_immigration_pop = np.matmul(mseries_nat_leslies, m_immigration_intpop) 
        l_immigration_pop = np.matmul(lseries_nat_leslies, l_immigration_intpop) 
      
        h_immigration_sum = []
        for pop_mat in h_immigration_pop:
            h_immigration_sum.append(np.sum(pop_mat))
        
        m_immigration_sum = []
        for pop_mat in m_immigration_pop:
            m_immigration_sum.append(np.sum(pop_mat))
        
        l_immigration_sum = []
        for pop_mat in l_immigration_pop:
            l_immigration_sum.append(np.sum(pop_mat))

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

        

            
    
        
  
        
    
    

    







        ## update the first row with birth rates 




    


        ## Operations are with the Leslie Matricies 
        
        # P1 = L x P0; P2 = L^2 x P0; Pn = L^n x P0 

        

        ## Plot the predicted growth 
        
class Monkey(Population):  
    pass 

class Rat(Population): 
    pass 

class Fish(Population): 
    pass 

class Bacteria(Population): 
    pass 

## include how many years this is valid to 
## have accuracy as time increases 


## long term growth calc only contains 17 age groups, this assumption was made for the human spicies
## can use dictionaries to predict populations of other kinds, with smaller or large lifespans meaning more age groups are required 

## find a new and more accurate way to model population