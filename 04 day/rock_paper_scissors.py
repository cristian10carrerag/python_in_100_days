import random

user_choice = int(input("What do yoy choose? Type 0 for rock, 1 for paper and 2 for scissors: "))

pc_choice = random.randint(0, 2)

print(F"pc choice {pc_choice}")

if user_choice >= 3 or user_choice < 0: 
    print("You type an invalid number, You lose!")   

elif user_choice == 0 and pc_choice == 2:
    print("You win!")

elif user_choice == 2 and pc_choice == 0:
    print("You lose!")

elif pc_choice > user_choice:
    print("You lose")

elif pc_choice > user_choice:
    print("You win")

elif pc_choice == user_choice:
    print("It's a draw")