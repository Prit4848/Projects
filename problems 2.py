# write a check given number is nagative or positive

a = 12
print("given number is positive")if a > 0 else print("number is nagative")

# given number is even or odd

if a % 2 ==0:
    print("given number is even")
else:
    print("given number is odd")

# creat calculator
print("hello")
b =input("enter number:")
c =input("enter operator(+ - * /):")
d =input("enter number:")

if c == "+":
    print(b + d)
elif c =="-":
    print(b - d)
elif c =="*":
    print(b * d)
elif c == "/":
    print(b / d)
else:
    print("invalid choice")

# enter leter wovel or not

e = "e"
if e in "aeiou" or e in "AEIOU":
    print("cheracter is vowel")
else:
    print("charecter is not vowel")

# wich is type of digit you have enter that check

num=int(input("enter the number 5 digit:"))

if num >=0 and num <10:
    print("number 1 digit")
elif num >=10 and num <100:
    print("number is 2 digit")
elif num >=100 and num <1000:
    print("number is 3 digit")
elif num >=1000 and num <10000:
    print("number is 4 digit")
elif num >=10000 and num <100000:
    print("number is 5 digit")
