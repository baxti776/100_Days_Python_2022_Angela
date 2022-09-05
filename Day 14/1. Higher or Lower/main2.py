import art
from data import data
from random import randint

user_find = True
user_score = 0
first_random = data[randint(0, 49)]['follower_count']


def compare():
    next_random = data[randint(0, 49)]['follower_count']
    if first_random > next_random:
        print(f"You find. Your score: {user_score}")

    print(f"{first_random}=={next_random}")


compare()
# while user_find:
