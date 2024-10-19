
def get_number(num):
    
    while True:
        user_number = input("Number" + str(num) +": ")
        try:
            number  = float(user_number)
            return number
        except ValueError:
            print("Invalid operand.please try again.")

while True:
    
    number1 = get_number(1)
    number2 = get_number(2)
    
    while True:
        signs = ['+','-','*','/']
        user_sign  = input("Sign:(+,-,*,/): ")
        if user_sign in signs:
            break
        else:
            print("Invalid sign, Please try again.")
            continue
        
    result = 0

    if user_sign == "+":
        result = number1 + number2
        
    elif user_sign == "-":
        result = number1 - number2
    
    elif user_sign == "*":
        result = number1 * number2
        
    elif user_sign == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            print("Division by zero.")
                    
    result = print(f"result: {result}")
    
    another_cals = input("Do you want to make another calculation?(y/n): ").lower()
    if another_cals == "y":
        continue
    else:
        break