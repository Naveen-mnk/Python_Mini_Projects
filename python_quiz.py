print('welcome to python quiz!')

def play():
    while True:
        user_play = input("Do you want to play?(yes/no): ").lower()
        if user_play == 'yes':
            print("okay, Let's play :)")
            return True
        else:
            print("Exit!")
            break

def questions():
    while True:

        score = 0

        print("\n**instructions: Enter the options only. \
            **need to score 50% to pass this test.\n")
        
        Q1 = input("1.What is the correct file extension for Python files? \
                A) .pt B) .py C) .pyt D) .python\n Answer: ").lower()
        if Q1 == "b":
            print("Correct answer")
            score += 1
        else:
            print("Wrong answer")
        
        Q2 = input("2.Which of the following is a valid variable name in Python? \
                A) 1st_variable B) first-variable C) first_variable D) first variable\n Answer: ").lower()
        if Q2 == "c":
            print("Correct answer")
            score += 1
        else:
            print("Wrong answer")
        
        Q3 = input("3.What will the following code output? print(type(5)) \
                A) <class 'float'> B) <class 'int'> C) <class 'str'> D) <class 'number'>\n Answer: ").lower()
        if Q3 == "b":
            print("Correct answer")
            score += 1
        else:
            print("Wrong answer")

        Q4 = input("4.Which keyword is used to define a function in Python? \
                A) func B) define C) def D) function\n Answer: ").lower()
        if Q4 == "c":
            print("Correct answer")
            score += 1
        else:
            print("Wrong answer")
        print(f"Your score is: {score}")
        print(f"Total percentage: {(score/ 4) * 100}%")

        if score >= 2:
            print("Congratulations you passed the test!")
            break
        else:
            redo_test = input("Need to score 50% to pass the test, Do you want to continue? (yes/no): ").lower()
            if redo_test == 'yes':
                continue
            else:
                print("Thanks for taking test")
                break

def main():
    if play():
        questions()



main()