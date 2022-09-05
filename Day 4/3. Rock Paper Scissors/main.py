import images
import random

print("0 for Rock, 1 for Paper, 2 for Scissors.")
user_option = int(input("Enter your option:"))

options = ['rock', 'paper', 'scissors']
random_int = random.randint(0, len(options) - 1)
if user_option == random_int:
    print("Equal")
elif (user_option == 0 and random_int == 1) or (user_option == 1 and random_int == 2) or (user_option == 2 and random_int == 0):
    print(f"You lose. Computer wins {options[user_option]} <==> {options[random_int]}")

else:
    print(f"You win, Computer lose. {options[user_option]} <==> {options[random_int]}")

    #
    # elif user_option == 0 and computer_option == 2:
    #     print(f"You win, Computer lose. {user_option} <==> {computer_option}")
    # elif user_option == 1 and computer_option == 0:
    #     print(f"fYou won, Computer lose, {user_option} <==> {computer_option}")
    # elif user_option == 2 and computer_option == 1:
    #     print("You win")
# print(random_choose)
# print(images.rock)
