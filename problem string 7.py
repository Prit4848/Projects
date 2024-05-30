# take an input from user as a astring then reverse it

# a = str(input("enter any atring:"))
# print(a[::-1])



# write a program to check if string contains only digits

# c ="1234"
#
# print(c.isdigit())

# write a program to check if string palindrom
# b = input("enter any string:")
# store = b
# d = (b[::-1])
# if d == store:
#     print("string is palindrom")
# else:
#     print("string is not palindrom")
# write a program to find number of vowel in a string
# a = input("enter the string :")
# vowel = 0
# for i in a:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         vowel += 1
# print("curent string vowel is:",vowel)

# write every word in string begins with capital letter
a = input("enter string :")
b = (a.title())
if a == b:
    print("every word string begins with capital")
else:
    print("every word string not begins with capital")