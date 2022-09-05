# user_number = int(input("Enter your number: "))
#
# for number in range(2, user_number):
#     if user_number % number == 0:
#         print(f"{user_number} is not a prime number")
#         break
# else:
#     print(f"{user_number} is a prime number.")


def prime_checker(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("Prime")
    else:
        print("Not Prime")


prime_checker(7)
