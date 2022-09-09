import random

difficulty = input("Please choose difficulty level 'hard' or 'easy': ")

random_int = random.randint(1, 100)


# print(f"Random int: {random_int}")


def easy_guess():
    chances = 10
    while chances > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess != random_int:
            chances -= 1
        if user_guess == random_int:
            print(f"You find it. \nYou have left {chances} chances.")
        elif chances == 0:
            print("You lose.")
            print(f"The hidden number was: {random_int}")
        elif user_guess > random_int:
            print(f"Too high. \nYou have left {chances} chances.")
        elif user_guess < random_int:
            print(f"Too low. \nYou have left {chances} chances.")


def hard_guess():
    chances = 5
    while chances > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess != random_int:
            chances -= 1
        if user_guess == random_int:
            print(f"You find it. \nYou have left {chances} chances.")
        elif chances == 0:
            print("You lose.")
            print(f"The hidden number was: {random_int}")
        elif user_guess > random_int:
            print(f"Too high. \nYou have left {chances} chances.")
        elif user_guess < random_int:
            print(f"Too low. \nYou have left {chances} chances.")


if difficulty == 'hard':
    print(f"You have got 5 chances")
    hard_guess()
elif difficulty == 'easy':
    print(f"You have got 10 chances")
    easy_guess()
else:
    print("You type smth wrong.")
