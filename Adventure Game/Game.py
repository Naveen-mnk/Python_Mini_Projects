
def Game():
    name = input("Enter your name: ").upper()
    print(f"Hello, {name}. Welcome to the Advanture game.")
    
    while True:

        play = input("Do you want to play? ").lower()
        if play == "yes" or play =="y":
            print("Game started..")
        else:
            print("Game ended")
            break
            
        first_choice = input("Do you want to turn 'left' or 'right'? ").lower()
        if first_choice == "left":
            print("You Turned left and moving.")
        elif first_choice == "right":
            print("There is a pathhole in right, you failed.")
            break
        else:
            print("Invalid choice, please enter the valid choice.")
            continue
        second_choice = input("There is a river infront of you, Do you want to 'swim' or use 'boat': ").lower()
        if second_choice == "swim":
            print("You got gold in the river, You Won...")
            break
        elif second_choice == "boat":
            print("you got nothing, you lost...")
            break
        else:
            print("Invalid Choice, please enter valid choice.")
            continue
   
Game()     