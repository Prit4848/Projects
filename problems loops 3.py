# write a program to find a sum of all even number
# sum = 0
# for i in range(0,51):
#     if i % 2 == 0:
#         sum = sum+i
# print(sum)

# write a program to write first 20 numbers and their squared numbers
# for a in range(1,21):
#     print(a,"squared=",a**2)

# write a program to find sum of 10 odd numbers using while loop
# a = 0
# sum = 0
# while a <= 10:
#     if a % 2 != 0:
#         sum += a
#     a += 1
# print(sum)

# write a program to check if number is divisible by 8 and 12 to 100 numbers

# for i in range(1,101):
#     if i % 8 == 0 and i % 12 == 0:
#       print(i)

# write a program to create a billing system at supermarket
while True:
    name = input("customer name:")
    total = 0
    while True:
        print("enter amount and quentity")
        quantity = float(input("enter quantity  of projuct:"))
        amount = float(input("enter amount of product:"))
        total += amount * quantity
        reapeat = input("add another product(yes/no) :")

        if reapeat == "no" or reapeat == "No":
            break

    print("-"*40)
    print("name:",name)
    print("Total",total)
    print("**********thank you for shoping**********")
    print("-"*40)
    reapeat1 = input("another customer(yes/no):")
    if reapeat1 == "no" or reapeat1 == "No":
        break




