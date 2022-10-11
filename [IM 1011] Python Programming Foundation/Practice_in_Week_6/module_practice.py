from game import guess

user_choice = input()
computer_choice = guess.figure_guess()

if user_choice == computer_choice:
    print(f'Your choice is {user_choice} and computer chose {computer_choice}. Tie.')
elif user_choice != computer_choice:
    if user_choice == 'paper' and computer_choice == 'scissors':
        print(f'Your choice is {user_choice} and computer chose {computer_choice}. Lose.')
    elif user_choice == 'paper' and computer_choice == 'stone':
        print(f'Your choice is {user_choice} and computer chose {computer_choice}. Win.')
    elif user_choice == 'scissors' and computer_choice == 'stone':
        print(f'Your choice is {user_choice} and computer chose {computer_choice}. Lose.')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print(f'Your choice is {user_choice} and computer chose {computer_choice}. Win.')
    elif user_choice == 'stone' and computer_choice == 'paper':
        print(f'Your choice is {user_choice} and computer chose {computer_choice}. Lose.')
    elif user_choice == 'stone' and computer_choice == 'scissors':
        print(f'Your choice is {user_choice} and computer chose {computer_choice}. Win.')
