fruits = ["apple","mango","banana"]
print(type(fruits))

# list slicing
a = ["iron man","thor","captain america","hulk","loki","spider man"]
print(a[2:4])
print(a[:4])
print(a[1:])
print(a[2::2])
print(a[::-1])
print(a[-3])
print(a[-1:-5:-1])

# list iteration
# for i in a:
#     print(i)
# find range
# for i in range(len(a)):
#     print(a[i])   # i change than find index values

# using while loop
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# using short hand for loop
[print(i) for i in a]

# list functions
# print(len(a)) # find the lenght
#
# print(a.count("iron man"))  # count how many time reapeat
#
# print(a.insert(1,"agent romanoff"))
# print(a.append("doctor strange"))  # using add new value in list
# print(a)
#
# print(a.remove("hulk"))
# print(a.pop(0)) # using the remove element of the list
# print(a)

# b = a.copy() # copy element
# print(b)
#
# print(a.index("iron man")) # find the index of given element
#
# c = ["hokai","natasha"]
# a.extend(c)  # extend of given list add other list element
# print(a)
#
# a.reverse() # reverse list
# print(a)
#
# a.sort() # sorting list asending order
# print(a)
#
# a.clear()
# print(a)  # clear all element

# list comprehansion
l1 =[1,2,3,4,5]
l2 = []

for i  in l1:
    if i > 3:
       l2.append(i)

print(l2,"\n",l1)

l3 = [i for i in l2 if i > 1]
print(l3)