# a = ("apple","mango","banana",23,2.2)
# print(type(a))
# # tuples are imutable
# b = ("ironman",)
# print(type(tuple))

# slicing and ittretion
a = ("oneplus","realme","samsung","nokia","iphone")
#
# print(a[1:3])
# print(a[:3])
# print(a[1::2])
# print(a[::-1])
# print(a[:-1:])
# print(a[2::-1])

# using for loop
for i in a:
    print(i)
# using for loop range
for i in range(len(a)):
    print(a[i])

# using while loop

i = 0

while i < len(a):
    print(a[i])
    i += 1

# convirsinon of tuples and tuples function

a = ("prit","chirag","ritesh")
print(type(a))
a = list(a)
print("after conversion",type(a))
print(a)

a.append("hardik")
print(type(a))
print(a)
print(a.count("prit"))
print("the index of the prit:",a.index("prit"))