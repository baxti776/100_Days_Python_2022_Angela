height = int(input("Enter your age in centimetres: "))
if height > 120:
    print("You can ride.")
    age = int(input("Enter your age: "))

    if age <= 18:
        print("You will pay 7$ to enter")
    elif age > 18 and age < 45:
        print("You will pay 12$")
    elif age >= 45 and age <= 55:
        print("You can ride for free.")
else:
    print("You can't ride")
