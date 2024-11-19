# Exceptions handle errors created by users in a way that doesn't break the code.

# Errors the computer can catch:
# zero division, file not found, value error, type error, index error,

class NegativeNumberError(Exception):
    

while True:
    try:
        num = int(input("Tell me a number: "))
    
    except TypeError:
        print("That wasn't a whole number.")
        continue

    else:
        break

while True:
    try:
        num2 = int(input("Tell me another number: "))
    
    except TypeError:
        print("That wasn't a whole number.")
        continue
    
    else:
        try:
            print(f'{str(num)} over {str(num2)} equals {str(num / num2)}')
        
        except ZeroDivisionError:
            print("You can't divide by zero.")
            continue

        again = input("Do you want to go again? (Y/N): ").upper().strip()

        if again == "Y":
            continue

        elif again == "N": 
            break
        
        else:
            break