# def hello(*name):  # arbitary argument
#     print("hello my name is",name[0])
# hello("prit","sachin","dhoni")
#
#
# def add(x,y):
#     print(x+y)
# add(12,23)
#
# def area(lenght,width):
#     print("area of rectengle",lenght*width)
# area(23,22)
#
#
#
# # parameters and argument
#
#
# # return statment
#
# def h(a,b):
#     return a + b
# print("the addition of two numbers",h(12,33))
#
# # recursion function
# def he():
#     print("hello")
#     return he()
# print(he())

def fact(f):
    for i in range(1,f):
        f = f * i
    return f
print(fact(4))

def fact1(f):
    if f == 1:
        return 1
    else:
        return f*fact1(f-1)
print(fact1(23))