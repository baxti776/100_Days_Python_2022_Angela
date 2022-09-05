import random

names = input("Enter the name: ")
names = names.split(", ")
random_choice = random.randint(0, len(names) - 1)
print(random_choice)
print(names[random_choice])
print(f"{names[random_choice]} will pay the bill.")
