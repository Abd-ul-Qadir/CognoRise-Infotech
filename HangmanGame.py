import random

lives = 6
words = ['pakistan','india','iran','iraq','china']

selected_word = random.choice(words)

print('\n\n\n********************************************************************************')
print('*********************************** Hangman GAME *******************************')
print('********************************************************************************')

display = ['_'] * selected_word.__len__()
print(f'\n{display}\n')
game_over = False

while not game_over:
    if lives == 6:
        print("\t|******|")
        print("\t|      |")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("==========================")
        print("***************************\n")
        
    guessed = input('Guess a letter: ').lower()
    print('\n\n') 
    if guessed in selected_word:
        
        for index in range(0, len(selected_word)):
            letter = selected_word[index]
            if letter == guessed:
                display[index] = guessed
    
    if guessed not in selected_word:
        lives -= 1
        if  lives == 0:
            print('You lose!!!!!')
            print('Complete word : ' , selected_word.upper() )
            game_over = True
    
    if  '_' not in display:
        print("Congratulations! You won the game.")
        print('Complete word : ' , selected_word.upper() )
        game_over = True
    
    print(display)
    
    print('\n')

    if lives == 5:
        print("\t|******|")
        print("\t|      |")
        print("\t|      O")
        print("\t|            ")
        print("\t|           ")
        print("\t|")
        print("\t|")
        print("==========================")
        print("***************************\n")
    
    if lives == 4:
        print("\t|******|")
        print("\t|      |")
        print("\t|      O")
        print("\t|     /")
        print("\t|")
        print("\t|")
        print("\t|")
        print("==========================")
        print("***************************\n")
    
    if lives == 3:
        print("\t|******|")
        print("\t|      |")
        print("\t|      O")
        print("\t|     /|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("==========================")
        print("***************************\n")
    
    if lives == 2:
        print("\t|******|")
        print("\t|      |")
        print("\t|      O")
        print("\t|     /|\\")
        print("\t|")
        print("\t|")
        print("\t|")
        print("==========================")
        print("***************************\n")
    
    if lives == 1:
        print("\t|******|")
        print("\t|      |")
        print("\t|      O")
        print("\t|     /|\\")
        print("\t|     /")
        print("\t|")
        print("\t|")
        print("===========================")
        print("***************************\n")
    
    if lives == 0:
        print("\t|******|")
        print("\t|      |")
        print("\t|      O")
        print("\t|     /|\\")
        print("\t|     / \\")
        print("\t|")
        print("==========================")
        print("***************************\n")
        