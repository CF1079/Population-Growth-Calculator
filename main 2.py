

def download_materials():
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'numpy'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'matplotlib'])

import numpy as np
from time import sleep
from numpy.linalg import matrix_power
from numpy import linalg as LA
from matplotlib import pyplot as plt
from art import *

def start_menu():
 tprint("Welcome to the\nMatrix Calculator!")
 print("************************************************************************************************")
 print("\n Copyright © of Charlie Falk, 2021")
 print("\n Built for the IA1 Specialists Maths PSMT")
 print("\n************************************************************************************************")
 sleep(1)
 print("Here are your options: \n [s] = Simple Operations \n [c] = Complex Operations \n [p] = Practical Operations \n [h] = Help" )
 sleep(0.7)
 choosing = (input("\n What do you need???: "))
 while choosing != 'p' and choosing != 'c' and choosing != 's' and choosing != 'h':
     print('Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n')
     sleep(0.3)
     print('Please Try Again')
     sleep(0.4)
     print("\n Here are your options: \n \n \n [s] = Simple Operations \n [c] = Complex Operations \n [p] = Practical Operations")
     choosing = (input("\n What do you need???: "))
 if(choosing == 'p'):
     print(' \n \n Your Choice Is >>> Practical Matrix Operations')
     Practical_Menu()
 elif(choosing == 'c'):
     print(' \n \n Your Choice Is >>> Complex Matrix Operations')

 elif(choosing == 's'):
     print(' \n \n Your Choice Is >>> Simple Matrix Operations')
     Simple_Menu()
 elif(choosing == 'h'):
     print(' \n \n Your Choice Is >>> Help')

def Simple_Menu():
    sleep(0.4)
    print(" \n Simple Matrix Calculator Options: \n[a] 'Addition' \n[s] 'Subtraction'\n [t] 'Transpose' ")
    sleep(0.4)
    Lesie_type = input(" What do you want?>> ")
    while Lesie_type != 'l' and Lesie_type != 'c':
     print("Incorrect Respone!")
     sleep(0.4)
     print("Try Again")
     sleep(0.5)
     print(" How would you like to go about This? \n type 'Basic' to input variables to calculate population \n type 'Complex' for a manual nxn input calculator")
     Lesie_type = input(" What do you want?>>")
    if (Lesie_type == 'l'):
     print("Your Choice is >>> Leslie Matrix Calculator")
     Simple_Leslie_Matrix_Calc()
    elif(Lesie_type == 'o'):
     print("Your Choice is >>> Other Matrix Calculator")

def Complex_Menu():
    print("Complex Menu")

def Practical_Menu():
    sleep(0.4)
    print(" \n Practical Matrix Calculator Options: \n[l] = Simple Leslie Matrix Calculator (guided) \n[c] = Complex Leslie Matrix Calculator (guided) \n[g] = Long Term Growth Calculator \n[m] = Manual Input Leslie Matrix Calculator")
    sleep(0.4)
    Lesie_type = input(" What do you want?>> ")
    while Lesie_type != 'l' and Lesie_type != 'c' and Lesie_type != 'g' and Lesie_type != 'm':
     print("Incorrect Respone!")
     sleep(0.4)
     print("Try Again")
     sleep(0.5)
     print(" How would you like to go about This? \n type 'Basic' to input variables to calculate population \n type 'Complex' for a manual nxn input calculator")
     Lesie_type = input(" What do you want?>>")
    if (Lesie_type == 'l'):
     print("Your Choice is >>> Simple Leslie Matrix Calculator")
     Simple_Leslie_Matrix_Calc()
    elif(Lesie_type == 'c'):
     print("Your Choice is >>> Complex Leslie Matrix Calculator")
     Complex_Leslie_Matrix_Calc()
    elif(Lesie_type == 'g'):
     Long_Term_Growth_Calc()
     print("Your Choice is >>> Long Term Growth Calculator")
    elif(Lesie_type == 'm'):
     print("Your Choice is >>> Manual Input Leslie Matrix Calculator")
     Manual_Input_Leslie()

def Simple_Leslie_Matrix_Calc():
 print("Please Define Scale of Leslie Matrix (n x n)  ")
 print(" [1] = 3x3 \n [2] = 4x4 \n[3] = 5x5 \n[4] = 6x6 \n[5] = 7x7 \n[6] = 8x8\n[7] = 9x9 \n[8] = 10x10 \n[9] = 18x18")
 Les_Size = input("What Size Do You need?: ")
 while Les_Size != '1' and Les_Size != '2' and Les_Size != '3' and Les_Size != '4' and Les_Size != '5' and Les_Size != '6' and Les_Size != '7' and Les_Size != '8' and Les_Size != '9' and Les_Size != '10' :
    print("Incorrect Response!\nIncorrect Response\nIncorrect Response")
    sleep(0.5)
    print('Please Try Again')
    print(" [1] = 3x3 \n [2] = 4x4 \n[3] = 5x5 \n[4] = 6x6 \n[5] = 7x7 \n[6] = 8x8\n[7] = 9x9 \n[8] = 10x10 ")
    Les_Size = input("What Size Do You need?: ")
 if Les_Size == '1':

   print("\nPlease input the following to generate leslie matrix")
   survival_rate1 = float(input("Survival Rate For Age Bracket 1: "))
   survival_rate2 = float(input("Survival Rate For Age Bracket 2: "))

   birthrate1 = float(input("Birth Rate for Age 1: "))
   birthrate2 = float(input("Birth Rate for Age 2: "))
   birthrate3 = float(input("Birth Rate for Age 3: "))

   Matrix1 = np.array([ [birthrate1,birthrate2,birthrate3],[survival_rate1,0,0],[0,survival_rate2,0] ])
   print("Your Leslie Matrix is....")
   print(Matrix1)

   int_pop1 = float(input("Initial Population Age 1: "))
   int_pop2 = float(input("Initial Population Age 2: "))
   int_pop3 = float(input("Initial Population Age 3: "))

   Matrix2 = np.array([ [int_pop1],[int_pop2],[int_pop3] ])
   print("Your Popluation Matrix is....")
   print(Matrix2)
   sleep(0.5)


   confirmation = input("Please Check Your Information and Confirm y/n: ")

   while confirmation != 'y' and confirmation != 'n':
     print('Invalid Input!')
     confirmation = input("Please Check Your Information and Confirm y/n: ")
     if confirmation == 'n':
      Simple_Leslie_Matrix_Calc()
     elif confirmation == 'y':
        break

   print("Generating Population....")
   sleep(0.5)
   Population = Matrix1.dot(Matrix2)
   print("Here is the Total Population....")
   print(Population)


   exit_menu()

 elif Les_Size == '2':
    survival_rate1 = float(input("Survival Rate For Age Bracket 1: "))
    survival_rate2 = float(input("Survival Rate For Age Bracket 2: "))
    survival_rate3 = float(input("Survival Rate for Age Bracket 3: "))

    birthrate1 = float(input("Birth Rate for Age 1: "))
    birthrate2 = float(input("Birth Rate for Age 2: "))
    birthrate3 = float(input("Birth Rate for Age 3: "))
    birthrate4 = float(input("Birth Rate for Age 4: "))

    Matrix1 = np.array([ [birthrate1,birthrate2,birthrate3,birthrate4],[survival_rate1,0,0,0],[0,survival_rate2,0,0],[0,0,survival_rate3,0]])
    print("Your Leslie Matrix is....")
    print(Matrix1)

    int_pop1 = float(input("Initial Population Age 1: "))
    int_pop2 = float(input("Initial Population Age 2: "))
    int_pop3 = float(input("Initial Population Age 3: "))
    int_pop4 = float(input("Initial Population Age 4: "))

    Matrix2 = np.array([ [int_pop1],[int_pop2],[int_pop3],[int_pop4] ])
    print("Your Popluation Matrix is....")
    print(Matrix2)
    sleep(0.8)
    Generation = int(input("What Generation?: "))
    Matrix3 = np.linalg.matrix_power(Matrix1,Generation)
    Population = Matrix3.dot(Matrix2)
    print("Here is the Total Population....")
    for idx,val in enumerate(Population):
        print("population " + str(idx + 1) + " is: " + str(val) )
    sleep(2)
    print("And here is the Population Matrix At Generation " +str(Generation)+ ": ")
    print(Population)
    print(" ")
 elif Les_Size == '3':
     survival_rate1 = float(input("Survival Rate For Age Bracket 1: "))
     survival_rate2 = float(input("Survival Rate For Age Bracket 2: "))
     survival_rate3 = float(input("Survival Rate for Age Bracket 3: "))

     birthrate1 = float(input("Birth Rate for Age 1: "))
     birthrate2 = float(input("Birth Rate for Age 2: "))
     birthrate3 = float(input("Birth Rate for Age 3: "))
     birthrate4 = float(input("Birth Rate for Age 4: "))

     Matrix1 = np.array([[birthrate1, birthrate2, birthrate3, birthrate4], [survival_rate1, 0, 0, 0], [0, survival_rate2, 0, 0],[0, 0, survival_rate3, 0]])
     print("Your Leslie Matrix is....")
     print(Matrix1)

     int_pop1 = float(input("Initial Population Age 1: "))
     int_pop2 = float(input("Initial Population Age 2: "))
     int_pop3 = float(input("Initial Population Age 3: "))
     int_pop4 = float(input("Initial Population Age 4: "))

     Matrix2 = np.array([[int_pop1], [int_pop2], [int_pop3], [int_pop4]])
     print("Your Popluation Matrix is....")
     print(Matrix2)
     sleep(0.8)
     Population = Matrix1.dot(Matrix2)
     print("Here is the Total Population....")
     print(Population)
 elif Les_Size == '9':
    survival_rate1 = float(input("Survival Rate For Age Bracket 1: "))
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


    Matrix1 = np.array([ [birthrate1,birthrate2,birthrate3,birthrate4,birthrate5,birthrate6,birthrate7,birthrate8,birthrate9,birthrate10,birthrate11,birthrate12,birthrate13,birthrate14,birthrate15,birthrate16,birthrate17,birthrate18],[survival_rate1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,survival_rate2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,survival_rate3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,survival_rate4,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,survival_rate5,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,survival_rate6,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,survival_rate7,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,survival_rate8,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,survival_rate9,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,survival_rate10,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,survival_rate11,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,survival_rate12,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,survival_rate13,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,survival_rate14,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,survival_rate15,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,survival_rate16,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,survival_rate17,0] ])
    print("Your Leslie Matrix is....")
    print(Matrix1)

    int_pop1 = float(input("Initial Population Age Bracket 1: "))
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

    Matrix2 = np.array([ [int_pop1],[int_pop2],[int_pop3],[int_pop4],[int_pop5],[int_pop6],[int_pop7],[int_pop8],[int_pop9],[int_pop10],[int_pop11],[int_pop12],[int_pop13],[int_pop14],[int_pop15],[int_pop16],[int_pop17],[int_pop18] ])
    print("Your Popluation Matrix is....")
    print(Matrix2)
    sleep(0.8)
    Generation = int(input("What Generation?: "))
    Matrix3 = np.linalg.matrix_power(Matrix1,Generation)
    Population = Matrix3.dot(Matrix2)
    print("Here is the Total Population....")
    for idx,val in enumerate(Population):
        print("population " + str(idx + 1) + " is: " + str(val) )
    sleep(2)
    print("And here is the Population Matrix At Generation " +str(Generation)+ ": ")
    print(Population)
    print(" ")

def Complex_Leslie_Matrix_Calc():
  print("Coming Soon!")

def Long_Term_Growth_Calc():
    print("Please Define Scale of Leslie Matrix (n x n)")
    print(" [1] = 3x3 \n [2] = 4x4 \n[3] = 5x5 \n[4] = 6x6 \n[5] = 7x7 \n[6] = 8x8\n[7] = 9x9 \n[8] = 10x10 \n[9] =18x18 ")
    Les_Size = input("What Size Do You need?: ")
    while Les_Size != '1' and Les_Size != '2' and Les_Size != '3' and Les_Size != '4' and Les_Size != '5' and Les_Size != '6' and Les_Size != '7' and Les_Size != '8' and Les_Size != '9' and Les_Size != '10':
        print("Incorrect Response!\nIncorrect Response\nIncorrect Response")
        sleep(0.5)
        print('Please Try Again')
        print(" [1] = 3x3 \n [2] = 4x4 \n[3] = 5x5 \n[4] = 6x6 \n[5] = 7x7 \n[6] = 8x8\n[7] = 9x9 \n[8] = 10x10 ")
        Les_Size = input("What Size Do You need?: ")
    if Les_Size == '1':
        generations = []
        number = int(input("How many generations?: "))
        print("Enter Generations: ")
        for i in range(number):
            inputgens = int(input())
            generations.append(inputgens)

        print("Here are you selected generations:" + str(generations))
        x1 = generations
        sleep(0.5)
        print("\nPlease input the following to generate High Series leslie matrix")
        hsurvival_rate1 = float(input("High Series Survival Rate For Age Bracket 1: "))
        hsurvival_rate2 = float(input("High Series Survival Rate For Age Bracket 2: "))

        hbirthrate1 = float(input("High Series Birth Rate for Age 1: "))
        hbirthrate2 = float(input("High Series Birth Rate for Age 2: "))
        hbirthrate3 = float(input("High Series Birth Rate for Age 3: "))

        hMatrix1 = np.array([[hbirthrate1, hbirthrate2, hbirthrate3], [hsurvival_rate1, 0, 0], [0, hsurvival_rate2, 0]])
        print("Your High Series Leslie Matrix is....")
        print(hMatrix1)

        print("\nPlease input the following to generate Medium Series leslie matrix")
        msurvival_rate1 = float(input("Med Series Survival Rate For Age Bracket 1: "))
        msurvival_rate2 = float(input("Med Series Survival Rate For Age Bracket 2: "))

        mbirthrate1 = float(input("Med Series Birth Rate for Age 1: "))
        mbirthrate2 = float(input("Med Series Birth Rate for Age 2: "))
        mbirthrate3 = float(input("Med Series Birth Rate for Age 3: "))

        mMatrix1 = np.array([[mbirthrate1, mbirthrate2, mbirthrate3], [msurvival_rate1, 0, 0], [0, msurvival_rate2, 0]])
        print("Your Med Series Leslie Matrix is....")
        print(mMatrix1)

        print("\nPlease input the following to generate Low Series leslie matrix")
        lsurvival_rate1 = float(input("Low Series Survival Rate For Age Bracket 1: "))
        lsurvival_rate2 = float(input("Low Series Survival Rate For Age Bracket 2: "))

        lbirthrate1 = float(input("Low Series Birth Rate for Age 1: "))
        lbirthrate2 = float(input("Low Series Birth Rate for Age 2: "))
        lbirthrate3 = float(input("Low Series Birth Rate for Age 3: "))

        lMatrix1 = np.array([[lbirthrate1, lbirthrate2, lbirthrate3], [lsurvival_rate1, 0, 0], [0, lsurvival_rate2, 0]])
        print("Your Low Series Leslie Matrix is....")
        print(lMatrix1)

        print("\nPlease input the following to generate the Population Matrix")
        int_pop1 = float(input("Initial Population Age 1: "))
        int_pop2 = float(input("Initial Population Age 2: "))
        int_pop3 = float(input("Initial Population Age 3: "))

        Matrix2 = np.array([[int_pop1], [int_pop2], [int_pop3]])
        print("Your Popluation Matrix is....")
        print(Matrix2)
        sleep(0.5)

        print('Generating Natural Increase')

        hnatural_increase = np.array(
            [[hbirthrate1, hbirthrate2, hbirthrate3], [hsurvival_rate1, 0, 0], [0, hsurvival_rate2, 0]])
        mnatural_increase = np.array(
            [[mbirthrate1, mbirthrate2, mbirthrate3], [msurvival_rate1, 0, 0], [0, msurvival_rate2, 0]])
        lnatural_increase = np.array(
            [[lbirthrate1, lbirthrate2, lbirthrate3], [lsurvival_rate1, 0, 0], [0, lsurvival_rate2, 0]])

        hnatleslie = []
        for year in generations:
            hnatleslie.append(matrix_power(hnatural_increase, year))

        hnatpop = []
        for array in hnatleslie:
            hnatpop.append(array.dot(Matrix2))

        hnatfinal = []
        for arraypop in hnatpop:
            for minarray in arraypop:
                for value in minarray:
                    hnatfinal.append(value)

        mnatleslie = []
        for year in generations:
            mnatleslie.append(matrix_power(mnatural_increase, year))

        mnatpop = []
        for array in mnatleslie:
            mnatpop.append(array.dot(Matrix2))

        mnatfinal = []
        for arraypop in mnatpop:
            for minarray in arraypop:
                for value in minarray:
                    mnatfinal.append(value)

        lnatleslie = []
        for year in generations:
            lnatleslie.append(matrix_power(lnatural_increase, year))

        lnatpop = []
        for array in lnatleslie:
            lnatpop.append(array.dot(Matrix2))

        lnatfinal = []
        for arraypop in lnatpop:
            for minarray in arraypop:
                for value in minarray:
                    lnatfinal.append(value)

        hnatcoords = hnatfinal[0::3]
        mnatcoords = mnatfinal[0::3]
        lnatcoords = lnatfinal[0::3]
        print(hnatcoords)
        plt.plot(x1, hnatcoords, label='High Series')
        plt.plot(x1, mnatcoords, label='Medium Series')
        plt.plot(x1, lnatcoords, label='Low Series')
        plt.xlabel('Time(years)')
        plt.ylabel('Natural Increase')
        plt.title(f'Model of Natural Increase of Victoria for {len(generations)} Years')
        plt.legend()
        plt.show()

        print('Please Input the Following')

        hnim1 = float(input("High Series Net Interstate Migration Age 1: "))
        hnim2 = float(input("High Series Net Interstate Migration Age 2: "))
        hnim3 = float(input("High Series Net Interstate Migration Age 3: "))

        hnom1 = float(input("High Series Net Overseas Migration Age 1 : "))
        hnom2 = float(input("High Series Net Overseas Migration Age 2: "))
        hnom3 = float(input("High Series Net Overseas Migration Age 3: "))

        mnim1 = float(input("Medium Series Net Interstate Migration Age 1: "))
        mnim2 = float(input("Medium Series Net Interstate Migration Age 2: "))
        mnim3 = float(input("Medium Series Net Interstate Migration Age 3: "))

        mnom1 = float(input("Medium Series Net Overseas Migration Age 1 : "))
        mnom2 = float(input("Medium Series Net Overseas Migration Age 2: "))
        mnom3 = float(input("Medium Series Net Overseas Migration Age 3: "))

        lnim1 = float(input("Low Series Net Interstate Migration Age 1: "))
        lnim2 = float(input("Low Series Net Interstate Migration Age 2: "))
        lnim3 = float(input("MLow Series Net Interstate Migration Age 3: "))

        lnom1 = float(input("Low Series Net Overseas Migration Age 1 : "))
        lnom2 = float(input("Low Series Net Overseas Migration Age 2: "))
        lnom3 = float(input("Low Series Net Overseas Migration Age 3: "))

        hNIM = np.array([[hnim1], [hnim2], [hnim3]])
        hNOM = np.array([[hnom1], [hnom2], [hnom3]])
        mNIM = np.array([[mnim1], [mnim2], [mnim3]])
        mNOM = np.array([[mnom1], [mnom2], [mnom3]])
        lNIM = np.array([[lnim1], [lnim2], [lnim3]])
        lNOM = np.array([[lnom1], [lnom2], [lnom3]])

        hprehimmigrationtotal = hNIM + hNOM
        mpreimmigrationtotal = mNIM + mNOM
        lpreimmigrationtotal = lNIM + lNOM

        hMatrix4 = []
        for year in generations:
            hMatrix4.append(hprehimmigrationtotal + (8768 * (year - 1)))

        mMatrix4 = []
        for year in generations:
            mMatrix4.append(mpreimmigrationtotal - (1895 * (year - 1)))

        lMatrix4 = []
        for year in generations:
            lMatrix4.append(lpreimmigrationtotal - (2731 * (year - 1)))

        hseriesleslie = []
        for year in generations:
            hseriesleslie.append(matrix_power(np.array(
                [[hbirthrate1 + (0.0000118156 * (year - 1)), hbirthrate2 + (0.0000118156 * (year - 1)),
                  hbirthrate3 + (0.0000118156 * (year - 1))],
                 [hsurvival_rate1 + (0.0000254545 * (year - 1)), 0, 0],
                 [0, hsurvival_rate2 + (0.0000254545 * (year - 1)), 0]]), year))

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
            mseriesleslie.append(matrix_power(np.array(
                [[mbirthrate1, mbirthrate2, mbirthrate3],
                 [msurvival_rate1, 0, 0], [0, msurvival_rate2, 0]]), year))

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
            lseriesleslie.append(matrix_power(np.array(
                [[lbirthrate1 - (0.0000281844 * (year - 1)), lbirthrate2 - (0.0000281844 * (year - 1)),
                  lbirthrate3 - (0.0000281844 * (year - 1))],
                 [lsurvival_rate1 - (0.0000145455 * (year - 1)), 0, 0],
                 [0, lsurvival_rate2 - (0.0000145455 * (year - 1)), 0]]), year))

        lpopulationanswer = []
        for array in lseriesleslie:
            lpopulationanswer.append(array.dot(lMatrix4[i]))

        lfinalpop = []
        for larraypop in lpopulationanswer:
            for lminarray in larraypop:
                for lvalue in lminarray:
                    lfinalpop.append(lvalue)

        confirmation = input("Please Check Your Information and Confirm y/n: ")

        while confirmation != 'y' and confirmation != 'n':
            print('Invalid Input!')
            confirmation = input("Please Check Your Information and Confirm y/n: ")
            if confirmation == 'y':
                break
            elif confirmation == 'n':
                Long_Term_Growth_Calc()

        sleep(2)
        print("\n \nGenerating Graph....(High Series)")
        sleep(0.5)
        print("Exit Graph to Continue")
        hAge1 = hfinalpop[0::3]
        hAge2 = hfinalpop[1::3]
        hAge3 = hfinalpop[2::3]

        print(hAge1)

        # checked and good
        hy1 = hAge1
        hy2 = hAge2
        hy3 = hAge3
        plt.plot(x1, hy1, label='Age 1', marker='o')
        plt.plot(x1, hy2, label='Age 2', marker='o')
        plt.plot(x1, hy3, label='Age 3', marker='o')
        plt.xlabel('Generations')
        plt.ylabel('Population')
        plt.title(f'High Series Model of Population Growth for {len(generations)} Generations')
        plt.legend()
        plt.show()

        sleep(2)
        print("\n \nGenerating Graph....(Med Series)")
        sleep(0.5)
        print("Exit Graph to Continue")
        mAge1 = mfinalpop[0::3]
        mAge2 = mfinalpop[1::3]
        mAge3 = mfinalpop[2::3]

        # checked and good
        x1 = generations
        my1 = mAge1
        my2 = mAge2
        my3 = mAge3
        plt.plot(x1, my1, label='Age 1', marker='o')
        plt.plot(x1, my2, label='Age 2', marker='o')
        plt.plot(x1, my3, label='Age 3', marker='o')
        plt.xlabel('Generations')
        plt.ylabel('Population')
        plt.title(f'Medium Series Model of Population Growth for {len(generations)} Generations')
        plt.legend()
        plt.show()

        sleep(2)
        print("\n \nGenerating Graph....(Low Series)")
        sleep(0.5)
        print("Exit Graph to Continue")
        lAge1 = lfinalpop[0::3]
        lAge2 = lfinalpop[1::3]
        lAge3 = lfinalpop[2::3]

        # checked and good
        x1 = generations
        ly1 = lAge1
        ly2 = lAge2
        ly3 = lAge3
        plt.plot(x1, ly1, label='Age 1', marker='o')
        plt.plot(x1, ly2, label='Age 2', marker='o')
        plt.plot(x1, ly3, label='Age 3', marker='o')
        plt.xlabel('Generations')
        plt.ylabel('Population')
        plt.title(f'Low Series Model of Population Growth for {len(generations)} Generations')
        plt.legend()
        plt.show()

        hhopefully3 = []
        for hpop in hpopulationanswer:
            hhopefully3.append(sum(hpop))

        mhopefully3 = []
        for mpop in mpopulationanswer:
            mhopefully3.append(sum(mpop))

        lhopefully3 = []
        for lpop in lpopulationanswer:
            lhopefully3.append(sum(lpop))

        highseries = hhopefully3
        medseries = mhopefully3
        lowseries = lhopefully3
        plt.plot(x1, highseries, label='High Series')
        plt.plot(x1, medseries, label='Medium Series')
        plt.plot(x1, lowseries, label='Low Series')
        plt.xlabel('Time(years)')
        plt.ylabel('Population')
        plt.title(f'Model of Population Growth (Females Only) for {len(generations)} Years')
        plt.legend()
        plt.show()

        maleratio = float(input(" Male Ratio: "))
        femaleratio = float(input(" Female Ratio: "))
        maleperc = (maleratio / femaleratio)

        hmalepop = [i * maleperc for i in hhopefully3]
        mmalepop = [i * maleperc for i in mhopefully3]
        lmalepop = [i * maleperc for i in lhopefully3]

        plt.plot(x1, hmalepop, label='High Series')
        plt.plot(x1, mmalepop, label='Medium Series')
        plt.plot(x1, lmalepop, label='Low Series')
        plt.xlabel('Time(years)')
        plt.ylabel('Population')
        plt.title(f'Model of Population Growth (Males Only) for {len(generations)} Years')
        plt.legend()
        plt.show()

        htotal = [hmalepop[i] + hhopefully3[i] for i in range(len(hmalepop))]
        mtotal = [mmalepop[i] + mhopefully3[i] for i in range(len(mmalepop))]
        ltotal = [lmalepop[i] + lhopefully3[i] for i in range(len(lmalepop))]

        plt.plot(x1, htotal, label='High Series')
        plt.plot(x1, mtotal, label='Medium Series')
        plt.plot(x1, ltotal, label='Low Series')
        plt.xlabel('Time(years)')
        plt.ylabel('Population')
        plt.title(f'Model of Population Growth (Total) for {len(generations)} Years')
        plt.legend()
        plt.show()
        exit_menu()

    elif Les_Size == '2':
        generations = []
        number = int(input("How many generations?: "))
        print("Enter Generations: ")
        for i in range(number):
            inputgens = int(input())
            generations.append(inputgens)

        print("Here are you selected generations:" + str(generations))
        sleep(0.5)
        print("\nPlease input the following to generate leslie matrix")
        survival_rate1 = float(input("Survival Rate For Age Bracket 1: "))
        survival_rate2 = float(input("Survival Rate For Age Bracket 2: "))
        survival_rate3 = float(input("Survival Rate For Age Bracket 3: "))

        birthrate1 = float(input("Birth Rate for Age 1: "))
        birthrate2 = float(input("Birth Rate for Age 2: "))
        birthrate3 = float(input("Birth Rate for Age 3: "))
        birthrate4 = float(input("Birth Rate for Age 4: "))

        Matrix1 = np.array([[birthrate1, birthrate2, birthrate3, birthrate4], [survival_rate1, 0, 0,0], [0, survival_rate2, 0,0],[0,0, survival_rate3, 0]])
        print("Your Leslie Matrix is....")
        print(Matrix1)

        int_pop1 = float(input("Initial Population Age 1: "))
        int_pop2 = float(input("Initial Population Age 2: "))
        int_pop3 = float(input("Initial Population Age 3: "))
        int_pop4 = float(input("Initial Population Age 4: "))

        Matrix2 = np.array([[int_pop1], [int_pop2], [int_pop3], [int_pop4]])
        print("Your Popluation Matrix is....")
        print(Matrix2)
        sleep(0.5)
        Population = Matrix1.dot(Matrix2)
        print("Here is the Total Population....")
        print(Population)

        products = []
        for i in generations:
            products.append(matrix_power(Matrix1, i))

        # checked and good
        products2 = []
        for i in products:
            products2.append(i.dot(Matrix2))

        val1 = []
        for array in products2:
            for element in array:
                val1.append(element)

        confirmation = input("Please Check Your Information and Confirm y/n: ")

        while confirmation != 'y' and confirmation != 'n':
            print('Invalid Input!')
            confirmation = input("Please Check Your Information and Confirm y/n: ")
            if confirmation == 'y':
                break
            elif confirmation == 'n':
                Long_Term_Growth_Calc()

        print("\n \nGenerating Data....")
        sleep(0.5)

        print("| Gen # |      Age 1      |      Age 2      |      Age 3      |")
        lst = [list(x) for x in products2]

        for array in lst:
            print("| ", (lst.index(array)) + 1, "   |        ", array[0], " " * (3 - len((array[0]))),
                  "        |       ",
                  array[1], "        |", "       ", array[2], "|"      , array[3],         "|")

        sleep(2)
        print("\n \nGenerating Graph....")
        sleep(0.5)
        print("Exit Graph to Continue")
        Age1 = val1[0::4]
        Age2 = val1[1::4]
        Age3 = val1[2::4]
        Age4 = val1[3::4]
        x2 = [5,6,7,8,9,10]
        y5 = [1.9,1.9,1.9,1.9,1.9,1.9]

        x1 = generations
        y1 = Age1
        y2 = Age2
        y3 = Age3
        y4 = Age4
        plt.plot(x1, y1, label='Age 1')
        plt.plot(x1, y2, label='Age 2')
        plt.plot(x1, y3, label='Age 3')
        plt.plot(x1, y4, label='Age 4')
        plt.plot(x2, y5, label='Test Medium Series')
        plt.xlabel('Generations')
        plt.ylabel('Population')
        plt.title(f'Model of Population Growth for {len(generations)} Generations')
        plt.legend()
        plt.show()


        eigenvalue, eigenvector = LA.eig(Matrix1)
        eigenval = max(eigenvalue)
        #eigenvalpos = np.where(eigenval)
        #eigenvec = eigenvector[eigenvalpos]
        print(eigenval)

        #     allvecstogether.append(aelement)

        #cteigenvec = allvecstogether[::4]

        #print(acteigenvec)

        #eigenvaltopower = eigenval**generations
        #print(eigenvaltopower)
        #popgrowth2 = eigenvaltopower*acteigenvec
        #print(popgrowth2)



        hopefully = []
        for gen1 in generations:
            hopefully.append(matrix_power(Matrix1,gen1))
        print(hopefully)
        print("Hopefully")

        hopefully2 = []
        for powermatrix in hopefully:
            hopefully2.append(powermatrix.dot(Matrix2))

        print(hopefully2)
        print("Hopefully2")

        hopefully3 = []
        for pop in hopefully2:
            hopefully3.append(sum(pop))

        print(hopefully3)
        print("Hopefully3")


        z1 = hopefully3
        plt.plot(x1, z1, label='Total Population', marker='o')
        plt.xlabel('Time(years)')
        plt.ylabel('Population')
        plt.title(f'Model of Population Growth for {len(generations)} Years')
        plt.legend()
        plt.show()

    elif Les_Size == '9':

        generations = []
        number = int(input("How many generations?: "))
        print("Enter Generations: ")
        for i in range(number):
            inputgens = int(input())
            generations.append(inputgens)

        print("Here are you selected generations:" + str(generations))
        x1 = generations
        sleep(0.5)

        print("\nPlease input the following to generate High Series leslie matrix")
        survival_rate1 = float(input("Survival Rate For Age Bracket 1: "))
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
        print("Your Leslie Matrix is....")
        print(Matrix1)

        int_pop1 = float(input("Initial Population Age Bracket 1: "))
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
        print("Your Popluation Matrix is....")
        print(Matrix2)

        sleep(0.8)

        print('Generating Natural Increase')

        hnatleslie = []
        for year in generations:
            hnatleslie.append(matrix_power(np.array([[birthrate1 + (0.0000118156 * (year - 1)), birthrate2 + (0.0000118156 * (year - 1)), birthrate3 + (0.0000118156 * (year - 1)), birthrate4 + (0.0000118156 * (year - 1)), birthrate5 + (0.0000118156 * (year - 1)), birthrate6 + (0.0000118156 * (year - 1)), birthrate7 + (0.0000118156 * (year - 1)),
                             birthrate8 + (0.0000118156 * (year - 1)), birthrate9 + (0.0000118156 * (year - 1)), birthrate10 + (0.0000118156 * (year - 1)), birthrate11 + (0.0000118156 * (year - 1)), birthrate12 + (0.0000118156 * (year - 1)), birthrate13 + (0.0000118156 * (year - 1)), birthrate14 + (0.0000118156 * (year - 1)),
                             birthrate15 + (0.0000118156 * (year - 1)), birthrate16 + (0.0000118156 * (year - 1)), birthrate17 + (0.0000118156 * (year - 1)), birthrate18 + (0.0000118156 * (year - 1))],
                            [survival_rate1 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, survival_rate2 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, survival_rate3 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, survival_rate4 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, survival_rate5 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, survival_rate6 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, survival_rate7 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, survival_rate8 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, survival_rate9 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate10 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate11 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate12 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate13 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate14 + (0.0000254545 * (year - 1)), 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate15 + (0.0000254545 * (year - 1)), 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate16 + (0.0000254545 * (year - 1)), 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate17 + (0.0000254545 * (year - 1)), 0]]), year))

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
            mnatleslie.append(matrix_power(np.array([[birthrate1, birthrate2, birthrate3, birthrate4, birthrate5, birthrate6, birthrate7,
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
            lnatleslie.append(matrix_power(np.array([[birthrate1 - (0.0000281844 * (year - 1)), birthrate2 - (0.0000281844 * (year - 1)), birthrate3 - (0.0000281844 * (year - 1)), birthrate4 - (0.0000281844 * (year - 1)), birthrate5 - (0.0000281844 * (year - 1)), birthrate6 - (0.0000281844 * (year - 1)), birthrate7 - (0.0000281844 * (year - 1)),
                             birthrate8 - (0.0000281844 * (year - 1)), birthrate9 - (0.0000281844 * (year - 1)), birthrate10 - (0.0000281844 * (year - 1)), birthrate11, birthrate12 - (0.0000281844 * (year - 1)), birthrate13 - (0.0000281844 * (year - 1)), birthrate14 - (0.0000281844 * (year - 1)),
                             birthrate15 - (0.0000281844 * (year - 1)), birthrate16 - (0.0000281844 * (year - 1)), birthrate17 - (0.0000281844 * (year - 1)), birthrate18 - (0.0000281844 * (year - 1))],
                            [survival_rate1 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, survival_rate2 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, survival_rate3 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, survival_rate4 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, survival_rate5 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, survival_rate6 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, survival_rate7 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, survival_rate8 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, survival_rate9 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate10 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate11 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate12 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate13 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate14 - (0.0000145455*(year-1)), 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate15 - (0.0000145455*(year-1)), 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate16 - (0.0000145455*(year-1)), 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate17 - (0.0000145455*(year-1)), 0]]), year))

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

        print('Please Input the Following to consider NIM and NOM')

        nim1 = float(input(" Net Interstate Migration Age 1: "))
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

        print(hMatrix4)
        print('hMatrix4')

        mMatrix4 = []
        for year in generations:
            mMatrix4.append(preimmigrationtotal - (1895 * (year - 1)))

        lMatrix4 = []
        for year in generations:
            lMatrix4.append(preimmigrationtotal - (2731 * (year - 1)))

        hseriesleslie = []
        for year in generations:
            hseriesleslie.append(matrix_power(np.array([[birthrate1 + (0.0000118156 * (year - 1)), birthrate2 + (0.0000118156 * (year - 1)), birthrate3 + (0.0000118156 * (year - 1)), birthrate4 + (0.0000118156 * (year - 1)), birthrate5 + (0.0000118156 * (year - 1)), birthrate6 + (0.0000118156 * (year - 1)), birthrate7 + (0.0000118156 * (year - 1)),
                             birthrate8 + (0.0000118156 * (year - 1)), birthrate9 + (0.0000118156 * (year - 1)), birthrate10 + (0.0000118156 * (year - 1)), birthrate11 + (0.0000118156 * (year - 1)), birthrate12 + (0.0000118156 * (year - 1)), birthrate13 + (0.0000118156 * (year - 1)), birthrate14 + (0.0000118156 * (year - 1)),
                             birthrate15 + (0.0000118156 * (year - 1)), birthrate16 + (0.0000118156 * (year - 1)), birthrate17 + (0.0000118156 * (year - 1)), birthrate18 + (0.0000118156 * (year - 1))],
                            [survival_rate1 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, survival_rate2 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, survival_rate3 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, survival_rate4 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, survival_rate5 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, survival_rate6 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, survival_rate7 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, survival_rate8 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, survival_rate9 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate10 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate11 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate12 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate13 + (0.0000254545 * (year - 1)), 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate14 + (0.0000254545 * (year - 1)), 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate15 + (0.0000254545 * (year - 1)), 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate16 + (0.0000254545 * (year - 1)), 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate17 + (0.0000254545 * (year - 1)), 0]]), year))

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
            mseriesleslie.append(matrix_power(np.array([[birthrate1, birthrate2, birthrate3, birthrate4, birthrate5, birthrate6, birthrate7,
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
            lseriesleslie.append(matrix_power(np.array([[birthrate1 - (0.0000281844 * (year - 1)), birthrate2 - (0.0000281844 * (year - 1)), birthrate3 - (0.0000281844 * (year - 1)), birthrate4 - (0.0000281844 * (year - 1)), birthrate5 - (0.0000281844 * (year - 1)), birthrate6 - (0.0000281844 * (year - 1)), birthrate7 - (0.0000281844 * (year - 1)),
                             birthrate8 - (0.0000281844 * (year - 1)), birthrate9 - (0.0000281844 * (year - 1)), birthrate10 - (0.0000281844 * (year - 1)), birthrate11, birthrate12 - (0.0000281844 * (year - 1)), birthrate13 - (0.0000281844 * (year - 1)), birthrate14 - (0.0000281844 * (year - 1)),
                             birthrate15 - (0.0000281844 * (year - 1)), birthrate16 - (0.0000281844 * (year - 1)), birthrate17 - (0.0000281844 * (year - 1)), birthrate18 - (0.0000281844 * (year - 1))],
                            [survival_rate1 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, survival_rate2 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, survival_rate3 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, survival_rate4 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, survival_rate5 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, survival_rate6 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, survival_rate7 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, survival_rate8 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, survival_rate9 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate10 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate11 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate12 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate13 - (0.0000145455*(year-1)), 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate14 - (0.0000145455*(year-1)), 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate15 - (0.0000145455*(year-1)), 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate16 - (0.0000145455*(year-1)), 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, survival_rate17 - (0.0000145455*(year-1)), 0]]), year))

        lpopulationanswer = []
        for array in lseriesleslie:
            lpopulationanswer.append(array.dot(lMatrix4[i]))

        lfinalpop = []
        for larraypop in lpopulationanswer:
            for lminarray in larraypop:
                for lvalue in lminarray:
                         lfinalpop.append(lvalue)

        confirmation = input("Please Check Your Information and Confirm y/n: ")

        while confirmation != 'y' and confirmation != 'n':
            print('Invalid Input!')
            confirmation = input("Please Check Your Information and Confirm y/n: ")
            if confirmation == 'y':
                break
            elif confirmation == 'n':
                Long_Term_Growth_Calc()

        sleep(2)
        print("\n \nGenerating Graph....(High Series)")
        sleep(0.5)
        print("Exit Graph to Continue")
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


        print(hAge1)
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
        print("\n \nGenerating Graph....(Med Series)")
        sleep(0.5)
        print("Exit Graph to Continue")
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
        print("\n \nGenerating Graph....(Low Series)")
        sleep(0.5)
        print("Exit Graph to Continue")
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



        hhopefully3 = []
        for hpop in hpopulationanswer:
            hhopefully3.append(sum(hpop))

        mhopefully3 = []
        for mpop in mpopulationanswer:
            mhopefully3.append(sum(mpop))

        lhopefully3 = []
        for lpop in lpopulationanswer:
            lhopefully3.append(sum(lpop))

        highseries = hhopefully3
        medseries = mhopefully3
        lowseries = lhopefully3
        plt.plot(x1, highseries, label='High Series')
        plt.plot(x1, medseries, label='Medium Series')
        plt.plot(x1, lowseries, label='Low Series')
        plt.xlabel('Time(years)')
        plt.ylabel('Population')
        plt.title(f'Model of Population Growth (Females Only) for {len(generations)} Years')
        plt.legend()
        plt.show()

        maleratio = float(input(" Male Ratio: "))
        femaleratio = float(input(" Female Ratio: "))
        maleperc = (maleratio / femaleratio)

        hmalepop = [i * maleperc for i in hhopefully3]
        mmalepop = [i * maleperc for i in mhopefully3]
        lmalepop = [i * maleperc for i in lhopefully3]

        plt.plot(x1, hmalepop, label='High Series')
        plt.plot(x1, mmalepop, label='Medium Series')
        plt.plot(x1, lmalepop, label='Low Series')
        plt.xlabel('Time(years)')
        plt.ylabel('Population')
        plt.title(f'Model of Population Growth (Males Only) for {len(generations)} Years')
        plt.legend()
        plt.show()

        htotal = [hmalepop[i] + hhopefully3[i] for i in range(len(hmalepop))]
        mtotal = [mmalepop[i] + mhopefully3[i] for i in range(len(mmalepop))]
        ltotal = [lmalepop[i] + lhopefully3[i] for i in range(len(lmalepop))]

        plt.plot(x1, htotal, label='High Series')
        plt.plot(x1, mtotal, label='Medium Series')
        plt.plot(x1, ltotal, label='Low Series')
        plt.xlabel('Time(years)')
        plt.ylabel('Population')
        plt.title(f'Model of Population Growth (Total) for {len(generations)} Years')
        plt.legend()
        plt.show()
        exit_menu()

def Manual_Input_Leslie():
 import numpy as np

 m = int(input("Enter Number of Rows in Matrix: "))
 n = int(input("Enter Number of Coloumns in Matrix: "))

 Mat1 = []
 Mat1 = Mat1
 for i in range (0,m):
     Mat1.append([])
 for i in range (0,m):
     for j in range (0,n):
         Mat1[i].append(j)
         Mat1[i][j]=0
         print('entry in row: ', i+1,' column: ', j+1)
         Mat1[i][j] = float(input())

 Mat1 = np.array(Mat1)
 print(Mat1)
 p = int(input("Enter Number of Rows in Matrix: "))
 q = int(input("Enter Number of Columns in Matrix: "))

 Mat2 = []
 for i in range (0,p):
     Mat2.append([])
 for i in range (0,p):
     for j in range (0,q):
         Mat2[i].append(j)
         Mat2[i][j]=0
         print('entry in row: ', i+1,' column: ', j+1)
         Mat2[i][j] = float(input())

 Mat2 = np.array(Mat2)
 print(Mat2)



 products = Mat1.dot(Mat2)
 print(products)

def Help_Menu():
    print("Simple Operations \n  Overveiw: \nThe Simple Menu Provides Simple Operations \n\n Funcitons: \nTranspose = Manipulation....Addmore ")
    print("Simple Operations \n  Overveiw: \nThe Simple Menu Provides Simple Operations \n\n Funcitons: \nTranspose = Manipulation....Addmore ")
    print("Simple Operations \n  Overveiw: \nThe Simple Menu Provides Simple Operations \n\n Funcitons: \nTranspose = Manipulation....Addmore ")
    print("Simple Operations \n  Overveiw: \nThe Simple Menu Provides Simple Operations \n\n Funcitons: \nTranspose = Manipulation....Addmore ")
     #put in the graphs displayed

def exit_menu():
 sleep(1)
 print("Where do you want to go? ")
 print("[r] = redo leslie matrix calculation \n[p] = return to practical menu \n[m] return to main menu \n[q] quit")
 whats_next = input("Where are you going now?: ")
 while whats_next != 'r' and whats_next != 'p' and whats_next != 'm' and whats_next != 'q':
    print('Incorrect Response! \n Incorrect Response! \n Incorrect Response!')
    sleep(0.3)
    print('Please Try Again')
    sleep(0.4)
    print("Where do you want to go? ")
    print(" [p] = return to practical menu \n[m] return to main menu \n[q] quit")
    whats_next = (input("Where are you going now?: "))
 if (whats_next == 'r'):
    Simple_Leslie_Matrix_Calc()
 elif (whats_next == 'p'):
    Practical_Menu()
 elif (whats_next == 'm'):
    start_menu()
 elif (whats_next == 'q'):
  print("\n GoodBye:)")
  sleep(0.5)
  quit()

start_menu()








#HELP MENU
#in documentation put how the female half is only calculated first
#maths behind each calculation
#add in compounding growth of birth, pop, NIM, NOM, immigrants
#explain in help menu how the age bracket system works


#OTHER
#sharpen up graphs
#change table and fix up labelling
#change table and fix up labelling
#do a specific general check by printing out all the constituent matricies
#for the generations have an input range to consolidate having to put in 40 numberes
#move the three lines form the graph to the start of the observed trendline
