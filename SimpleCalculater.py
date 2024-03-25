calculation = True
while calculation:
    expresion = input('Enter expression (e.g 2 + 2 )(Press Q to Quit): ')
    
    if expresion.upper() =='Q':
        break
    
    if '+' in expresion:
        num1,num2 = expresion.split('+')
        num1 ,num2 = float(num1), float(num2)
        result= num1 + num2
    
    elif '-' in expresion:
        num1,num2 = expresion.split('-')
        num1 ,num2 = float(num1), float(num2)
        result= num1-num2
    
    elif '*' in expresion:
        num1,num2 = expresion.split('*')
        num1 ,num2 = float(num1), float(num2)
        result= num1*num2
    
    elif '/' in expresion:
        num1,num2 = expresion.split('/')
        num1 ,num2 = float(num1), float(num2)
        result= num1/num2
    
    else:
        print("Invalid input!!!!")
        continue
        
    print(f"The result of '{expresion}' is ",result)