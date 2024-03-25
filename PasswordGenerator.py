import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(characters, length))    
    return password

while True:
    
    user_input = input("Enter the desired length of the password(Press Q to Quit): ")
    
    if user_input.upper() == 'Q':
        break
    if user_input.isdigit():
        length = int(user_input)
        password = generate_password(length)
        print("Generated Password:", password)
    else:
        print("Enter digit only!!!! ")