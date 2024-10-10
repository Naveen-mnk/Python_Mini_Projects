import  random

ran_num = random.randint(1,100)

while True:
    try:
        guess = int(input("Guess the Number(1 - 100): "))

        if guess < ran_num:
            print("Too Low")
        elif guess == ran_num:
            print("Well Done!")
            break
        elif guess > ran_num:
            print("Too High")
    except ValueError:
        print("Enter Valid Number!")