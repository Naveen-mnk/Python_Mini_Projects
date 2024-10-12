import random

choice_dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissor'}
choices = ('r', 'p', 's')

def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, Scissor? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice! Please choose r, p, or s.')

def display_choice(user_choice, computer_choice):
    print(f'You chose: {choice_dict[user_choice]}')
    print(f'Computer chose: {choice_dict[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif ((user_choice == 'r' and computer_choice == 's') or
          (user_choice == 'p' and computer_choice == 'r') or
          (user_choice == 's' and computer_choice == 'p')):
        print('You Win!')
    else:
        print('You Lose!')

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choice(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        user_continue = input('Do you want to continue (y/n): ').lower()
        if user_continue == 'n':
            print("Thank you for playing!")
            break

play_game()
