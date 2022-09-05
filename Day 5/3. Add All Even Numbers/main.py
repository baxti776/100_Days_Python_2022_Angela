# sum_of_numbers = 0
# for number in range(0, 101, 2):
#     sum_of_numbers += number
# print(sum_of_numbers)

total = 0
for number in range(0, 101):
    if number % 2 == 0:
        total += number
print(total)
