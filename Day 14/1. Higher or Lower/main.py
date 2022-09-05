# import art
# from data import data
# from random import randint
#
# # print(data, logo)
#
# print(art.logo)
#
#
# def compare():
#     user_find = True
#     user_score = 0
#     while user_find:
#         first_random = data[randint(0, 49)]
#         second_random = data[randint(0, 49)]
#         first_follower = first_random['follower_count']
#         second_follower = second_random['follower_count']
#
#         print(f"Compare A: {first_random['name']}, {first_random['description']}, from {first_random['country']}.")
#         print(art.vs)
#         print(f"Compare B: {second_random['name']}, {second_random['description']}, from {second_random['country']}.")
#         print(f"Compare A:{first_follower}")
#         print(f"Compare B:{second_follower}")
#         players_option = input("Who has more followers? Type 'A' or 'B': ")
#         if first_follower > second_follower and players_option == 'A':
#             user_score += 1
#             print(f"You find. Your score: {user_score}.")
#         elif first_follower < second_follower and players_option == 'B':
#             user_score += 1
#             print(f"You find. Your score: {user_score}.")
#         else:
#             print("You cant find. \nTry again.")
#             user_find = False
#             print(f"Your score: {user_score}")
#
#
# compare()
