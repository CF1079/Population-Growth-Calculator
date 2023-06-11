__date_created__ = '11/06/2023'
__last_update__ = '11/06/2023'

__author__ = 'Charlie Falk'
__version__ = '0.01' 
__date__ = '11/06/2023'


import popmod 




def start_menu():
 tprint("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPopulation Growth Calculator!")
 print("************************************************************************************************")
 print("\n Copyright © of Charlie Falk, 2021")
 print("\n Built for the IA1 Specialists Maths PSMT")
 print("\n 40-year Projection of the Population of Victoria")
 print("\n************************************************************************************************")
 sleep(1)
 print("\nOptions \n\n[p] = Projections \n\n[d] = Documentation" )
 choosing = (input("\nWhat do you need???: "))
 while choosing != 'p' and choosing != 'd':
     print('Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n')
     sleep(0.3)
     print('Please Try Again')
     sleep(0.4)
     print("\n Here are your options: \n \n \n [p] = Projections \n [d] Documentation")
     choosing = (input(" What do you need???: "))
 if(choosing == 'p'):
     Long_Term_Growth_Calc()
 elif(choosing == 'd'):
     Documentation_Menu()

def Documentation_Menu():
   print("The Population Projection Calculator was created for the Specialist Maths IA1")
   print("\n It utilises matrix operations from the numpy library to generate a graph of a population projection")

def exit_menu():
 sleep(1)
 print("Where do you want to go? ")
 print("[r] = redo \n[m] = main menu \n[q] = quit")
 whats_next = input("Where are you going now?: ")
 while whats_next != 'r' and whats_next != 'm' and whats_next != 'q':
    print('Incorrect Response! \n Incorrect Response! \n Incorrect Response!')
    sleep(0.3)
    print('Please Try Again')
    sleep(0.4)
    print("Where do you want to go? ")
    print("[r] = redo \n[m] = main menu \n[q] = quit")
    whats_next = (input("Where are you going now?: "))
 if (whats_next == 'r'):
    Long_Term_Growth_Calc()
 elif (whats_next == 'm'):
    start_menu()
 elif (whats_next == 'q'):
  print("\n GoodBye:)")
  sleep(0.5)
  quit()


