import random
from time import sleep

print('-----------------Welcome to Dice Rolling Simulator-----------------\n')
rolling = True 

while rolling:
    try:
        sides = int(input('\nEnter the number of sides on Dice : '))
        rolls = int(input('How many times want to roll Dice  : '))
        
        for  i in range(rolls):
            num = random.randint(1,sides)
            sleep(1)
            print("Roll ",i+1," : ",num)
        
        choice = input("\nDo you want to continue (y/n)? ")
        if choice.lower() == "n":
            print('\n------------------------------Exiting--------------------------\n\n')
            break
    except ValueError:
        print('Please  enter a valid input')