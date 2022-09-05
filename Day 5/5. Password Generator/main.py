# Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
space = ""
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_password_letters = random.choices(letters, weights=None, k=nr_letters)
random_password_numbers = random.choices(numbers, weights=None, k=nr_numbers)
random_password_symbols = random.choices(symbols, weights=None, k=nr_symbols)

# password = random_password_letters + random_password_numbers + random_password_symbols
password = []
password.extend(random_password_symbols + random_password_numbers + random_password_letters)
easy_password = space.join(password)

# hard_password = random.shuffle(random_password_symbols + random_password_numbers + random_password_letters)
# hard_password = random.shuffle(easy_password)
print(password)
print(f"Easy password: {easy_password}")

hard_password = random.shuffle(password)
hard_password = space.join(password)
print(f"Hard password: {hard_password}")

# print(f"Hard password: {random_password_letters + random_password_numbers + random_password_symbols}")


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
