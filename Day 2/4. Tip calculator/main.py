print("Welcome to the tip calculator")
total_bill = float(input("Enter the total bill: "))
percentage = float(input("Enter the percentage of the tip. 12, 10, 15: "))
people = int(input("How many people will split the bill? "))

need_to_pay = round((((total_bill * percentage) / 100) + total_bill) / people, 2)
print(f"{need_to_pay}$")