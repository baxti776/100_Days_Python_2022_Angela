from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": subtract,
              "/": divide,
              "*": multiply,
              }


def calculation():
    print(logo)
    num1 = float(input("Enter your first number: "))
    for operation in operations:
        print(operation)
    should_continue = True
    while should_continue:
        operation = input("Enter your operation:  ")
        num2 = float(input("Enter your next number: "))
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        if input("Type 'y'  or 'n': ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculation()


calculation()
# operation = input("Pick another operation")
# num3 = int(input("Enter number: "))
# calculation_function = operations[operation]
# second_answer = calculation_function(first_answer, num3)
# print(f"{first_answer} {operation} {num3} = {second_answer}")
