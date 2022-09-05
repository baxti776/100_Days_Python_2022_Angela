name1 = input("Enter your name: ")
name2 = input("Enter your name: ")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
lower_names = lower_name1 + lower_name2
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
true = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
love = l + o + v + e
love_score = str(true) + str(love)
love_score = int(love_score)

if love_score < 10 | love_score > 90:
    print(f"Your score is {love_score}, you go like coke and mentos")
elif love_score >= 40 & love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
