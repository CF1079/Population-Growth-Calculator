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

    
    def simulate_growth(self, year: int): 

        # access data from csv 
        initial_populations = np.array([]) # np.array containing all of the age groups initial population values 
        survival_rates = np.array([]) # list containing all of the age groups survival rates 
        birth_rates = np.array([]) # list containing all of the age groups birth rates 
       
        for index in range(self._num_age_groups):
            initial_populations = np.append(initial_populations, self._popdb.get_pop_data(index, ['initial_population']))
            survival_rates = np.append(survival_rates, self._popdb.get_pop_data(index, ['survival_rate']))
            birth_rates = np.append(birth_rates, self._popdb.get_pop_data(index, ['birth_rate']))

        # format data 
        initial_populations = initial_populations.reshape(self._num_age_groups,1)
        survival_rates = survival_rates[0:-1]      

        # create leslie matrix from this data 
        leslie_matrix = np.zeros((self._num_age_groups - 1, self._num_age_groups - 1))
        leslie_matrix[np.diag_indices_from(leslie_matrix)] = survival_rates
        leslie_matrix = np.append(leslie_matrix, np.zeros((self._num_age_groups-1,1)), axis=1)
        leslie_matrix = np.vstack([birth_rates, leslie_matrix])
        
        # multiply leslie matrix (to the nth power) and population matrix 
        
        
        population_calculated = np.matmul((np.linalg.matrix_power(leslie_matrix, year)) , initial_populations)
        
        
        print(population_calculated)
        

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

## long term growth calc only contains 17 age groups, this assumption was made for the human spicies
## can use dictionaries to predict populations of other kinds, with smaller or large lifespans meaning more age groups are required 

popdb = PopDB('test_database.csv')
popsim = Human(popdb)
print(popsim.simulate_growth(25))
print(popsim.simulate_growth(26))

def Long_Term_Growth_Calc():
    generations = []
    number = int(input("How many years will be projected?: "))
    print("Enter each year individually: ")
    for i in range(number):
        inputgens = int(input())
        generations.append(inputgens)
    x1 = generations
    sleep(0.5)

    print("\nPlease input the following to generate High Series leslie matrix")
    survival_rate1 = float(input("\nSurvival Rate For Age Bracket 1: "))
    survival_rate2 = float(input("Survival Rate For Age Bracket 2: "))
    survival_rate3 = float(input("Survival Rate for Age Bracket 3: "))
    survival_rate4 = float(input("Survival Rate For Age Bracket 4: "))
    survival_rate5 = float(input("Survival Rate For Age Bracket 5: "))
    survival_rate6 = float(input("Survival Rate for Age Bracket 6: "))
    survival_rate7 = float(input("Survival Rate For Age Bracket 7: "))
    survival_rate8 = float(input("Survival Rate For Age Bracket 8: "))
    survival_rate9 = float(input("Survival Rate for Age Bracket 9: "))
    survival_rate10 = float(input("Survival Rate For Age Bracket 10: "))
    survival_rate11 = float(input("Survival Rate For Age Bracket 11: "))
    survival_rate12 = float(input("Survival Rate for Age Bracket 12: "))
    survival_rate13 = float(input("Survival Rate For Age Bracket 13: "))
    survival_rate14 = float(input("Survival Rate For Age Bracket 14: "))
    survival_rate15 = float(input("Survival Rate for Age Bracket 15: "))
    survival_rate16 = float(input("Survival Rate For Age Bracket 16: "))
    survival_rate17 = float(input("Survival Rate For Age Bracket 17: "))

    birthrate1 = float(input("Birth Rate for Age 1: "))
    birthrate2 = float(input("Birth Rate for Age 2: "))
    birthrate3 = float(input("Birth Rate for Age 3: "))
    birthrate4 = float(input("Birth Rate for Age 4: "))
    birthrate5 = float(input("Birth Rate for Age 5: "))
    birthrate6 = float(input("Birth Rate for Age 6: "))
    birthrate7 = float(input("Birth Rate for Age 7: "))
    birthrate8 = float(input("Birth Rate for Age 8: "))
    birthrate9 = float(input("Birth Rate for Age 9: "))
    birthrate10 = float(input("Birth Rate for Age 10: "))
    birthrate11 = float(input("Birth Rate for Age 11: "))
    birthrate12 = float(input("Birth Rate for Age 12: "))
    birthrate13 = float(input("Birth Rate for Age 13: "))
    birthrate14 = float(input("Birth Rate for Age 14: "))
    birthrate15 = float(input("Birth Rate for Age 15: "))
    birthrate16 = float(input("Birth Rate for Age 16: "))
    birthrate17 = float(input("Birth Rate for Age 17: "))
    birthrate18 = float(input("Birth Rate for Age 18: "))

    Matrix1 = np.array([[birthrate1, birthrate2, birthrate3, birthrate4, birthrate5, birthrate6, birthrate7,
                         birthrate8, birthrate9, birthrate10, birthrate11, birthrate12, birthrate13, birthrate14,
                         birthrate15, birthrate16, birthrate17, birthrate18],
                        [survival_rate1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, survival_rate2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, survival_rate3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, survival_rate4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, survival_rate5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, survival_rate6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, survival_rate7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, survival_rate8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, survival_rate9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate10, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate11, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate12, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate13, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate14, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate15, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate16, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate17, 0]])
    print("\n\nYour Leslie Matrix is....")
    sleep(1)
    print(Matrix1)

    int_pop1 = float(input("\n\nInitial Population Age Bracket 1: "))
    int_pop2 = float(input("Initial Population Age Bracket 2: "))
    int_pop3 = float(input("Initial Population Age Bracket 3: "))
    int_pop4 = float(input("Initial Population Age Bracket 4: "))
    int_pop5 = float(input("Initial Population Age Bracket 5: "))
    int_pop6 = float(input("Initial Population Age Bracket 6: "))
    int_pop7 = float(input("Initial Population Age Bracket 7: "))
    int_pop8 = float(input("Initial Population Age Bracket 8: "))
    int_pop9 = float(input("Initial Population Age Bracket 9: "))
    int_pop10 = float(input("Initial Population Age Bracket 10: "))
    int_pop11 = float(input("Initial Population Age Bracket 11: "))
    int_pop12 = float(input("Initial Population Age Bracket 12: "))
    int_pop13 = float(input("Initial Population Age Bracket 13: "))
    int_pop14 = float(input("Initial Population Age Bracket 14: "))
    int_pop15 = float(input("Initial Population Age Bracket 15: "))
    int_pop16 = float(input("Initial Population Age Bracket 16: "))
    int_pop17 = float(input("Initial Population Age Bracket 17: "))
    int_pop18 = float(input("Initial Population Age Bracket 18: "))

    Matrix2 = np.array(
        [[int_pop1], [int_pop2], [int_pop3], [int_pop4], [int_pop5], [int_pop6], [int_pop7], [int_pop8], [int_pop9],
         [int_pop10], [int_pop11], [int_pop12], [int_pop13], [int_pop14], [int_pop15], [int_pop16], [int_pop17],
         [int_pop18]])
    print("\n\nYour Popluation Matrix is....")
    sleep(1)
    print(Matrix2)

    sleep(0.8)

    print('\nGenerating graph of Natural Increase....')
    print("Exit Graph to Continue")
    sleep(1)


    hnatleslie = []
    for year in generations:
        hnatleslie.append(matrix_power(np.array([[birthrate1 + (0.0000118156 * (year - 1)),
                                                  birthrate2 + (0.0000118156 * (year - 1)),
                                                  birthrate3 + (0.0000118156 * (year - 1)),
                                                  birthrate4 + (0.0000118156 * (year - 1)),
                                                  birthrate5 + (0.0000118156 * (year - 1)),
                                                  birthrate6 + (0.0000118156 * (year - 1)),
                                                  birthrate7 + (0.0000118156 * (year - 1)),
                                                  birthrate8 + (0.0000118156 * (year - 1)),
                                                  birthrate9 + (0.0000118156 * (year - 1)),
                                                  birthrate10 + (0.0000118156 * (year - 1)),
                                                  birthrate11 + (0.0000118156 * (year - 1)),
                                                  birthrate12 + (0.0000118156 * (year - 1)),
                                                  birthrate13 + (0.0000118156 * (year - 1)),
                                                  birthrate14 + (0.0000118156 * (year - 1)),
                                                  birthrate15 + (0.0000118156 * (year - 1)),
                                                  birthrate16 + (0.0000118156 * (year - 1)),
                                                  birthrate17 + (0.0000118156 * (year - 1)),
                                                  birthrate18 + (0.0000118156 * (year - 1))],
                                                 [survival_rate1 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, survival_rate2 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, survival_rate3 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, survival_rate4 + (0.0000254545 * (year - 1)), 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, survival_rate5 + (0.0000254545 * (year - 1)), 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, survival_rate6 + (0.0000254545 * (year - 1)), 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, survival_rate7 + (0.0000254545 * (year - 1)), 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, survival_rate8 + (0.0000254545 * (year - 1)),
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate9 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0,
                                                  0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate10 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                  0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate11 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                  0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate12 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate13 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate14 + (0.0000254545 * (year - 1)), 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate15 + (0.0000254545 * (year - 1)), 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate16 + (0.0000254545 * (year - 1)), 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate17 + (0.0000254545 * (year - 1)), 0]]), year))

    hnatanswer = []
    for array in hnatleslie:
        hnatanswer.append(array.dot(Matrix2))

    hnatfinal = []
    for harraypop in hnatanswer:
        for hminarray in harraypop:
            for hvalue in hminarray:
                hnatfinal.append(hvalue)

    mnatleslie = []
    for year in generations:
        mnatleslie.append(matrix_power(
            np.array([[birthrate1, birthrate2, birthrate3, birthrate4, birthrate5, birthrate6, birthrate7,
                       birthrate8, birthrate9, birthrate10, birthrate11, birthrate12, birthrate13, birthrate14,
                       birthrate15, birthrate16, birthrate17, birthrate18],
                      [survival_rate1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, survival_rate2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, survival_rate3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, survival_rate4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, survival_rate5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, survival_rate6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, survival_rate7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, survival_rate8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, survival_rate9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate10, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate11, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate12, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate13, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate14, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate15, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate16, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate17, 0]]), year))

    mnatanswer = []
    for array in mnatleslie:
        mnatanswer.append(array.dot(Matrix2))

    mnatfinal = []
    for marraypop in mnatanswer:
        for mminarray in marraypop:
            for mvalue in mminarray:
                mnatfinal.append(mvalue)

    lnatleslie = []
    for year in generations:
        lnatleslie.append(matrix_power(np.array([[birthrate1 - (0.0000281844 * (year - 1)),
                                                  birthrate2 - (0.0000281844 * (year - 1)),
                                                  birthrate3 - (0.0000281844 * (year - 1)),
                                                  birthrate4 - (0.0000281844 * (year - 1)),
                                                  birthrate5 - (0.0000281844 * (year - 1)),
                                                  birthrate6 - (0.0000281844 * (year - 1)),
                                                  birthrate7 - (0.0000281844 * (year - 1)),
                                                  birthrate8 - (0.0000281844 * (year - 1)),
                                                  birthrate9 - (0.0000281844 * (year - 1)),
                                                  birthrate10 - (0.0000281844 * (year - 1)), birthrate11,
                                                  birthrate12 - (0.0000281844 * (year - 1)),
                                                  birthrate13 - (0.0000281844 * (year - 1)),
                                                  birthrate14 - (0.0000281844 * (year - 1)),
                                                  birthrate15 - (0.0000281844 * (year - 1)),
                                                  birthrate16 - (0.0000281844 * (year - 1)),
                                                  birthrate17 - (0.0000281844 * (year - 1)),
                                                  birthrate18 - (0.0000281844 * (year - 1))],
                                                 [survival_rate1 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, survival_rate2 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, survival_rate3 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, survival_rate4 - (0.0000145455 * (year - 1)), 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, survival_rate5 - (0.0000145455 * (year - 1)), 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, survival_rate6 - (0.0000145455 * (year - 1)), 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, survival_rate7 - (0.0000145455 * (year - 1)), 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, survival_rate8 - (0.0000145455 * (year - 1)),
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate9 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0, 0, 0,
                                                  0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate10 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                  0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate11 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                  0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate12 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate13 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate14 - (0.0000145455 * (year - 1)), 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate15 - (0.0000145455 * (year - 1)), 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate16 - (0.0000145455 * (year - 1)), 0, 0],
                                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  survival_rate17 - (0.0000145455 * (year - 1)), 0]]), year))

    lnatanswer = []
    for array in lnatleslie:
        lnatanswer.append(array.dot(Matrix2))

    lnatfinal = []
    for larraypop in lnatanswer:
        for lminarray in larraypop:
            for lvalue in lminarray:
                lnatfinal.append(lvalue)

    hnatcoords = hnatfinal[0::18]
    mnatcoords = mnatfinal[0::18]
    lnatcoords = lnatfinal[0::18]



    plt.plot(x1, hnatcoords, label='High Series')
    plt.plot(x1, mnatcoords, label='Medium Series')
    plt.plot(x1, lnatcoords, label='Low Series')
    plt.xlabel('Time(years)')
    plt.ylabel('Natural Increase')
    plt.title(f'Model of Natural Increase of Victoria for {len(generations)} Years')
    plt.legend()
    plt.show()

    print('\n\nPlease Input the Following to consider NIM and NOM')

    nim1 = float(input(" \n Net Interstate Migration Age 1: "))
    nim2 = float(input(" Net Interstate Migration Age 2: "))
    nim3 = float(input(" Net Interstate Migration Age 3: "))
    nim4 = float(input(" Net Interstate Migration Age 4: "))
    nim5 = float(input(" Net Interstate Migration Age 5: "))
    nim6 = float(input(" Net Interstate Migration Age 6: "))
    nim7 = float(input(" Net Interstate Migration Age 7: "))
    nim8 = float(input(" Net Interstate Migration Age 8: "))
    nim9 = float(input(" Net Interstate Migration Age 9: "))
    nim10 = float(input(" Net Interstate Migration Age 10: "))
    nim11 = float(input(" Net Interstate Migration Age 11: "))
    nim12 = float(input(" Net Interstate Migration Age 12: "))
    nim13 = float(input(" Net Interstate Migration Age 13: "))
    nim14 = float(input(" Net Interstate Migration Age 14: "))
    nim15 = float(input(" Net Interstate Migration Age 15: "))
    nim16 = float(input(" Net Interstate Migration Age 16: "))
    nim17 = float(input(" Net Interstate Migration Age 17: "))
    nim18 = float(input(" Net Interstate Migration Age 18: "))

    nom1 = float(input(" Net Overseas Migration Age 1: "))
    nom2 = float(input(" Net Overseas Migration Age 2: "))
    nom3 = float(input(" Net Overseas Migration Age 3: "))
    nom4 = float(input(" Net Overseas Migration Age 4: "))
    nom5 = float(input(" Net Overseas Migration Age 5: "))
    nom6 = float(input(" Net Overseas Migration Age 6: "))
    nom7 = float(input(" Net Overseas Migration Age 7: "))
    nom8 = float(input(" Net Overseas Migration Age 8: "))
    nom9 = float(input(" Net Overseas Migration Age 9: "))
    nom10 = float(input(" Net Overseas Migration Age 10: "))
    nom11 = float(input(" Net Overseas Migration Age 11: "))
    nom12 = float(input(" Net Overseas Migration Age 12: "))
    nom13 = float(input(" Net Overseas Migration Age 13: "))
    nom14 = float(input(" Net Overseas Migration Age 14: "))
    nom15 = float(input(" Net Overseas Migration Age 15: "))
    nom16 = float(input(" Net Overseas Migration Age 16: "))
    nom17 = float(input(" Net Overseas Migration Age 17: "))
    nom18 = float(input(" Net Overseas Migration Age 18: "))

    NIM = np.array(
        [[nim1], [nim2], [nim3], [nim4], [nim5], [nim6], [nim7], [nim8], [nim9],
         [nim10], [nim11], [nim12], [nim13], [nim14], [nim15], [nim16], [nim17],
         [nim18]])
    NOM = np.array(
        [[nom1], [nom2], [nom3], [nom4], [nom5], [nom6], [nom7], [nom8], [nom9],
         [nom10], [nom11], [nom12], [nom13], [nom14], [nom15], [nom16], [nom17],
         [nom18]])

    npreimmigrationtotal = NIM + NOM
    preimmigrationtotal = npreimmigrationtotal + Matrix2

    hMatrix4 = []
    for year in generations:
        hMatrix4.append(preimmigrationtotal + (8768 * (year - 1)))

    mMatrix4 = []
    for year in generations:
        mMatrix4.append(preimmigrationtotal - (1895 * (year - 1)))

    lMatrix4 = []
    for year in generations:
        lMatrix4.append(preimmigrationtotal - (2731 * (year - 1)))

    hseriesleslie = []
    for year in generations:
        hseriesleslie.append(matrix_power(np.array([[birthrate1 + (0.0000118156 * (year - 1)),
                                                     birthrate2 + (0.0000118156 * (year - 1)),
                                                     birthrate3 + (0.0000118156 * (year - 1)),
                                                     birthrate4 + (0.0000118156 * (year - 1)),
                                                     birthrate5 + (0.0000118156 * (year - 1)),
                                                     birthrate6 + (0.0000118156 * (year - 1)),
                                                     birthrate7 + (0.0000118156 * (year - 1)),
                                                     birthrate8 + (0.0000118156 * (year - 1)),
                                                     birthrate9 + (0.0000118156 * (year - 1)),
                                                     birthrate10 + (0.0000118156 * (year - 1)),
                                                     birthrate11 + (0.0000118156 * (year - 1)),
                                                     birthrate12 + (0.0000118156 * (year - 1)),
                                                     birthrate13 + (0.0000118156 * (year - 1)),
                                                     birthrate14 + (0.0000118156 * (year - 1)),
                                                     birthrate15 + (0.0000118156 * (year - 1)),
                                                     birthrate16 + (0.0000118156 * (year - 1)),
                                                     birthrate17 + (0.0000118156 * (year - 1)),
                                                     birthrate18 + (0.0000118156 * (year - 1))],
                                                    [survival_rate1 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, survival_rate2 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, survival_rate3 + (0.0000254545 * (year - 1)), 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, survival_rate4 + (0.0000254545 * (year - 1)), 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, survival_rate5 + (0.0000254545 * (year - 1)), 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, survival_rate6 + (0.0000254545 * (year - 1)), 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, survival_rate7 + (0.0000254545 * (year - 1)),
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate8 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate9 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate10 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0,
                                                     0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate11 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0,
                                                     0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate12 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0,
                                                     0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate13 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate14 + (0.0000254545 * (year - 1)), 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate15 + (0.0000254545 * (year - 1)), 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate16 + (0.0000254545 * (year - 1)), 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate17 + (0.0000254545 * (year - 1)), 0]]), year))

    hpopulationanswer = []
    for array in hseriesleslie:
        hpopulationanswer.append(array.dot(hMatrix4[i]))

    hfinalpop = []
    for harraypop in hpopulationanswer:
        for hminarray in harraypop:
            for hvalue in hminarray:
                hfinalpop.append(hvalue)

    mseriesleslie = []
    for year in generations:
        mseriesleslie.append(matrix_power(
            np.array([[birthrate1, birthrate2, birthrate3, birthrate4, birthrate5, birthrate6, birthrate7,
                       birthrate8, birthrate9, birthrate10, birthrate11, birthrate12, birthrate13, birthrate14,
                       birthrate15, birthrate16, birthrate17, birthrate18],
                      [survival_rate1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, survival_rate2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, survival_rate3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, survival_rate4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, survival_rate5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, survival_rate6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, survival_rate7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, survival_rate8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, survival_rate9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate10, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate11, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate12, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate13, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate14, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate15, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate16, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate17, 0]]), year))

    mpopulationanswer = []
    for array in mseriesleslie:
        mpopulationanswer.append(array.dot(mMatrix4[i]))

    mfinalpop = []
    for marraypop in mpopulationanswer:
        for mminarray in marraypop:
            for mvalue in mminarray:
                mfinalpop.append(mvalue)

    lseriesleslie = []
    for year in generations:
        lseriesleslie.append(matrix_power(np.array([[birthrate1 - (0.0000281844 * (year - 1)),
                                                     birthrate2 - (0.0000281844 * (year - 1)),
                                                     birthrate3 - (0.0000281844 * (year - 1)),
                                                     birthrate4 - (0.0000281844 * (year - 1)),
                                                     birthrate5 - (0.0000281844 * (year - 1)),
                                                     birthrate6 - (0.0000281844 * (year - 1)),
                                                     birthrate7 - (0.0000281844 * (year - 1)),
                                                     birthrate8 - (0.0000281844 * (year - 1)),
                                                     birthrate9 - (0.0000281844 * (year - 1)),
                                                     birthrate10 - (0.0000281844 * (year - 1)), birthrate11,
                                                     birthrate12 - (0.0000281844 * (year - 1)),
                                                     birthrate13 - (0.0000281844 * (year - 1)),
                                                     birthrate14 - (0.0000281844 * (year - 1)),
                                                     birthrate15 - (0.0000281844 * (year - 1)),
                                                     birthrate16 - (0.0000281844 * (year - 1)),
                                                     birthrate17 - (0.0000281844 * (year - 1)),
                                                     birthrate18 - (0.0000281844 * (year - 1))],
                                                    [survival_rate1 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, survival_rate2 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, survival_rate3 - (0.0000145455 * (year - 1)), 0, 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, survival_rate4 - (0.0000145455 * (year - 1)), 0, 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, survival_rate5 - (0.0000145455 * (year - 1)), 0, 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, survival_rate6 - (0.0000145455 * (year - 1)), 0,
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, survival_rate7 - (0.0000145455 * (year - 1)),
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate8 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate9 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0, 0,
                                                     0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate10 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0,
                                                     0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate11 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0,
                                                     0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate12 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0,
                                                     0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate13 - (0.0000145455 * (year - 1)), 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate14 - (0.0000145455 * (year - 1)), 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate15 - (0.0000145455 * (year - 1)), 0, 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate16 - (0.0000145455 * (year - 1)), 0, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     survival_rate17 - (0.0000145455 * (year - 1)), 0]]), year))

    lpopulationanswer = []
    for array in lseriesleslie:
        lpopulationanswer.append(array.dot(lMatrix4[i]))

    lfinalpop = []
    for larraypop in lpopulationanswer:
        for lminarray in larraypop:
            for lvalue in lminarray:
                lfinalpop.append(lvalue)

    confirmation = input("\n\nPlease Check Your Information and Confirm y/n: ")

    while confirmation != 'y' and confirmation != 'n':
        print('Invalid Input!')
        confirmation = input("Please Check Your Information and Confirm y/n: ")
        if confirmation == 'y':
            break
        elif confirmation == 'n':
            Long_Term_Growth_Calc()

    sleep(2)
    print("\n \nGenerating Graph of High Series....")
    print("Exit Graph to Continue")
    sleep(1)
    hAge1 = hfinalpop[0::18]
    hAge2 = hfinalpop[1::18]
    hAge3 = hfinalpop[2::18]
    hAge4 = hfinalpop[3::18]
    hAge5 = hfinalpop[4::18]
    hAge6 = hfinalpop[5::18]
    hAge7 = hfinalpop[6::18]
    hAge8 = hfinalpop[7::18]
    hAge9 = hfinalpop[8::18]
    hAge10 = hfinalpop[9::18]
    hAge11 = hfinalpop[10::18]
    hAge12 = hfinalpop[11::18]
    hAge13 = hfinalpop[12::18]
    hAge14 = hfinalpop[13::18]
    hAge15 = hfinalpop[14::18]
    hAge16 = hfinalpop[15::18]
    hAge17 = hfinalpop[16::18]
    hAge18 = hfinalpop[17::18]

    # checked and good
    x1 = generations

    plt.plot(x1, hAge1, label='Age 1', marker='o')
    plt.plot(x1, hAge2, label='Age 2', marker='o')
    plt.plot(x1, hAge3, label='Age 3', marker='o')
    plt.plot(x1, hAge4, label='Age 4', marker='o')
    plt.plot(x1, hAge5, label='Age 5', marker='o')
    plt.plot(x1, hAge6, label='Age 6', marker='o')
    plt.plot(x1, hAge7, label='Age 7', marker='o')
    plt.plot(x1, hAge8, label='Age 8', marker='o')
    plt.plot(x1, hAge9, label='Age 9', marker='o')
    plt.plot(x1, hAge10, label='Age 10', marker='o')
    plt.plot(x1, hAge11, label='Age 11', marker='o')
    plt.plot(x1, hAge12, label='Age 12', marker='o')
    plt.plot(x1, hAge13, label='Age 13', marker='o')
    plt.plot(x1, hAge14, label='Age 14', marker='o')
    plt.plot(x1, hAge15, label='Age 15', marker='o')
    plt.plot(x1, hAge16, label='Age 16', marker='o')
    plt.plot(x1, hAge17, label='Age 17', marker='o')
    plt.plot(x1, hAge18, label='Age 18', marker='o')
    plt.xlabel('Generations')
    plt.ylabel('Population')
    plt.title(f'High Series Model of Population Growth for {len(generations)} Generations')
    plt.legend()
    plt.show()

    sleep(2)
    print("\n \nGenerating Graph of Med Series....")
    print("Exit Graph to Continue")
    sleep(1)
    mAge1 = mfinalpop[0::18]
    mAge2 = mfinalpop[1::18]
    mAge3 = mfinalpop[2::18]
    mAge4 = mfinalpop[3::18]
    mAge5 = mfinalpop[4::18]
    mAge6 = mfinalpop[5::18]
    mAge7 = mfinalpop[6::18]
    mAge8 = mfinalpop[7::18]
    mAge9 = mfinalpop[8::18]
    mAge10 = mfinalpop[9::18]
    mAge11 = mfinalpop[10::18]
    mAge12 = mfinalpop[11::18]
    mAge13 = mfinalpop[12::18]
    mAge14 = mfinalpop[13::18]
    mAge15 = mfinalpop[14::18]
    mAge16 = mfinalpop[15::18]
    mAge17 = mfinalpop[16::18]
    mAge18 = mfinalpop[17::18]

    plt.plot(x1, mAge1, label='Age 1', marker='o')
    plt.plot(x1, mAge2, label='Age 2', marker='o')
    plt.plot(x1, mAge3, label='Age 3', marker='o')
    plt.plot(x1, mAge4, label='Age 4', marker='o')
    plt.plot(x1, mAge5, label='Age 5', marker='o')
    plt.plot(x1, mAge6, label='Age 6', marker='o')
    plt.plot(x1, mAge7, label='Age 7', marker='o')
    plt.plot(x1, mAge8, label='Age 8', marker='o')
    plt.plot(x1, mAge9, label='Age 9', marker='o')
    plt.plot(x1, mAge10, label='Age 10', marker='o')
    plt.plot(x1, mAge11, label='Age 11', marker='o')
    plt.plot(x1, mAge12, label='Age 12', marker='o')
    plt.plot(x1, mAge13, label='Age 13', marker='o')
    plt.plot(x1, mAge14, label='Age 14', marker='o')
    plt.plot(x1, mAge15, label='Age 15', marker='o')
    plt.plot(x1, mAge16, label='Age 16', marker='o')
    plt.plot(x1, mAge17, label='Age 17', marker='o')
    plt.plot(x1, mAge18, label='Age 18', marker='o')
    plt.xlabel('Generations')
    plt.ylabel('Population')
    plt.title(f'Medium Series Model of Population Growth for {len(generations)} Generations')
    plt.legend()
    plt.show()

    sleep(2)
    print("\n \nGenerating Graph of Low Series....")
    print("Exit Graph to Continue")
    sleep(1)
    lAge1 = lfinalpop[0::18]
    lAge2 = lfinalpop[1::18]
    lAge3 = lfinalpop[2::18]
    lAge4 = lfinalpop[3::18]
    lAge5 = lfinalpop[4::18]
    lAge6 = lfinalpop[5::18]
    lAge7 = lfinalpop[6::18]
    lAge8 = lfinalpop[7::18]
    lAge9 = lfinalpop[8::18]
    lAge10 = lfinalpop[9::18]
    lAge11 = lfinalpop[10::18]
    lAge12 = lfinalpop[11::18]
    lAge13 = lfinalpop[12::18]
    lAge14 = lfinalpop[13::18]
    lAge15 = lfinalpop[14::18]
    lAge16 = lfinalpop[15::18]
    lAge17 = lfinalpop[16::18]
    lAge18 = lfinalpop[17::18]

    plt.plot(x1, lAge1, label='Age 1', marker='o')
    plt.plot(x1, lAge2, label='Age 2', marker='o')
    plt.plot(x1, lAge3, label='Age 3', marker='o')
    plt.plot(x1, lAge4, label='Age 4', marker='o')
    plt.plot(x1, lAge5, label='Age 5', marker='o')
    plt.plot(x1, lAge6, label='Age 6', marker='o')
    plt.plot(x1, lAge7, label='Age 7', marker='o')
    plt.plot(x1, lAge8, label='Age 8', marker='o')
    plt.plot(x1, lAge9, label='Age 9', marker='o')
    plt.plot(x1, lAge10, label='Age 10', marker='o')
    plt.plot(x1, lAge11, label='Age 11', marker='o')
    plt.plot(x1, lAge12, label='Age 12', marker='o')
    plt.plot(x1, lAge13, label='Age 13', marker='o')
    plt.plot(x1, lAge14, label='Age 14', marker='o')
    plt.plot(x1, lAge15, label='Age 15', marker='o')
    plt.plot(x1, lAge16, label='Age 16', marker='o')
    plt.plot(x1, lAge17, label='Age 17', marker='o')
    plt.plot(x1, lAge18, label='Age 18', marker='o')
    plt.xlabel('Generations')
    plt.ylabel('Population')
    plt.title(f'Low Series Model of Population Growth for {len(generations)} Generations')
    plt.legend()
    plt.show()

    htotal = [sum(hpopulationanswer[i]) for i in range(len(hpopulationanswer))]
    mtotal = [sum(mpopulationanswer[i]) for i in range(len(mpopulationanswer))]
    ltotal = [sum(lpopulationanswer[i]) for i in range(len(lpopulationanswer))]

    sleep(2)
    print("\n \nGenerating Graph of Total Population Growth....")
    print("Exit Graph to Continue")
    sleep(1)



    plt.plot(x1, htotal, label='High Series')
    plt.plot(x1, mtotal, label='Medium Series')
    plt.plot(x1, ltotal, label='Low Series')
    plt.xlabel('Time(years)')
    plt.ylabel('Population')
    plt.title(f'Model of Population Growth (Total) for {len(generations)} Years')
    plt.legend()
    plt.show()
    print("\n\n")

