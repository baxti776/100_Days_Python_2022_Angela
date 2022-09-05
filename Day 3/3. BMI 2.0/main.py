weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimetres: "))
height /= 100
BMI = weight / height ** 2
if height < 0 or weight < 0:
    print("You entered your data incorrectly")
else:
    if BMI < 18:
        print(f"Your BMI is {BMI} and you are underweight.")
    elif 18.5 < BMI and BMI < 25:
        print(f"Your BMI is {BMI} and you are normal weight.")
    elif 25 < BMI and BMI < 30:
        print(f"Your BMI is {BMI} and you are overweight.")
    elif 30 < BMI and BMI < 35:
        print(f"Your BMI is {BMI} and you are obese.")
    elif BMI > 35:
        print(f"Your BMI is {BMI} and you are clinically obese")
    else:
        print("None")

"""
under 18 underweight
over 18.5 but below 25 - normal weight
over 25 but below 30 - overweight
over 30 but below 35 - obese
over 35 - clinically obese
"""
