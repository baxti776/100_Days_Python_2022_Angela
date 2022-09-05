from MENU import MENU
import prettytable
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
user_option = input("What would you like? (espresso/latte/cappuccino): ")


def transaction():
    print("Please insert your coins.")
    quarters = float(input("Enter your quarters(0,25):")) * 0.25
    dimes = float(input("Enter your dimes(0,1):")) * 0.1
    nickles = float(input("Enter your nickles(0,05):")) * 0.05
    pennies = float(input("Enter your pennies(0,01):")) * 0.01
    all_sum = (quarters + dimes + nickles + pennies)



    change = all_sum - MENU['espresso']['cost']
    return all_sum
    return change


transaction()


def check_resources():
    print(f"Resources:\nWater: {resources['water']},"
          f"\nMilk: {resources['milk']},"
          f"\nCoffee: {resources['coffee']} ")


check_resources()
