import random

computer_wins = 0
human_wins= 0
round = 1
selection = ['rock', 'paper', 'scissor']
again = True
check_yes = lambda x: True if "y" in x else False

print('\n\n\n********************************************************************************')
print('***************************** ROCK PAPER SCISSOR GAME **************************')
print('********************************************************************************')

while again:
    print('\n----------------------------------------')
    print(f'*************** Round {round} ****************')
    print('----------------------------------------')

    print('\n----Press 1 for Rock.\n----Press 2 for Paper.\n----Press 3 for Scissor.')
    human_selection = selection[int(input("Enter your Choice : "))-1]
    
    print('\n')
    computer_selection = selection[random.randint(0,2)]
    
    if human_selection == computer_selection:
        print(f'----Tie!!!---- \n')
    
    elif human_selection == 'rock' and computer_selection ==  'scissor':
        print(f"Rock crushes Scissors..... You Win!!!")
        human_wins += 1
    
    elif human_selection == 'scissor' and computer_selection ==  'paper':
        print(f"Scissor cuts Paper..... You Win!!!")
        human_wins += 1
    
    elif human_selection == 'paper' and computer_selection ==  'rock':
        print(f"Paper covers Rock..... You Win!!!")
        human_wins += 1
    
    else:
        print(f" You Lose!!!")
        computer_wins += 1        
        
    print(f'\n----Computer Selection : {computer_selection}')
    print(f'----Human Selection    : {human_selection}')
    print("\n*******************************")
    print(f'----Computer Wins : {computer_wins} ----')
    print(f'----Human Wins    : {human_wins} ----')
    print("*******************************")
    again = check_yes(input("\nWant to play another Round?(Y/N) : ").lower())
    round += 1

print('------------------Exiting------------------')