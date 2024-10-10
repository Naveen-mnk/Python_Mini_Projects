
import random

choice_dict = { 'r' : 'Rock','p' : 'Paper','s' : 'Scissor'}
choices = ('r','p','s')

while True:
    user_choice = input('Rock,Paper,Scissor? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invalid Choice!')
        continue

    computer_choice = random.choice(choices)

    print(f'You chose: {choice_dict[user_choice]}')
    print(f'Computer chose: {choice_dict[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif ((user_choice == 'r' and computer_choice == 's') or
          (user_choice == 'p' and computer_choice == 'r') or
          (user_choice == 's' and computer_choice == 'p')):
        print('You Win')
    else:
        print('You Lose')

    user_continue = input('Do you want to continue (y/n): ').lower()
    if user_continue == 'n':
        print("Thank you for playing!")
        break