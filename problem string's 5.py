# to get fibonci serise
# f = int(input("enter to get fibonacci series:"))
# a = 0
# b = 1
# print(a)
# print(b)
# if f == 1:
#     print("the fibonacci series is :",f)
# else:
#     for i in range(2,f):
#         c = a + b
#         a = b
#         b = c
#         print(c)

# check the number iss prime or not
# num = int(input("enter the number then check the number is prime or not:"))
#
# if num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("number is not prime")
#             break
#         else:
#             print("number is prime")
# else:
#     print("number is not prime")

# check the numberis pallendrome
# num = int(input("enter the number:"))
# temp = num
# rev = 0
# while num > 0:
#      dig = num % 10
#      rev = rev*10+dig
#      num = num//10
# if rev == temp:
#     print("number is pallendrom")
# else:
#     print("number is not pallendrom")

# area calculator
print("----------area calculator---------")
print("-----------------------------------")
while True:
    print("press 1 to get area of square")
    print("press 2 to get area of rectangle")
    print("press 3 to get area of circle")
    print("press 4 to get area of triangle")


    choice = int(input("choice any one of (1-4): "))

    if choice == 1:
        side = float(input("enter the lenght of side: "))
        area = side**2
        print("the area of square is : ",area)
    elif choice == 2:
        height = float(input("enter the height of rectangle: "))
        width =  float(input("enter the witdh  of rectangle: "))
        area1 = height * width
        print("tht are of rectangle :",area1)
    elif choice == 3:
        radius = float(input("enter the radius of circle: "))
        r = radius**2
        area3 = 3.14*r
        print("the area of circle: ",area3)
    elif choice == 4:
        b = float(input("enter the base lenght of triangle: "))
        h = float(input("enter the height of base"))
        area4 = (b*h)/2
        print("the area of triangle: ",area4)
    else:
        print("invalid choice !!!")
    reapeat = input("you have reapeat this calculator (yes/no):")
    print("-"*30)
    if reapeat == "no":
        break




