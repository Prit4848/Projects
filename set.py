a = {"ironman","hulk","spider man","thor","captain america","vision","natasha"}
b = {"superman","bat-man","wonder-women"}
c = {"vision","natasha","hulk"}
d = {"vision","natasha","hulk"}
e = {"pikachu","raichu","sparrow","balba shore"}
print(a)
print(type(a))

# for x in a:
#     print(x)
#
# # set function part 1
# print(a.add("black panther")) # add function use
# print(a)
#
# print(a.pop()) # remove randam  elemnet
# print(a)
# print(a.remove("thor")) # remove first enter element
# print(a)
#
# print(a.discard("hulk"))
# print(a)

# c = a.copy()
# print(c)

# set function part 2
# print(a.isdisjoint(b))  # a all elemnt not in b and b all element not in a
#
# print(c.issubset(a))  # c all element in a and a
#
# print(a.issuperset(c))  # a is father of c
#
# print(a.update(b)) # add another set
# print(a)

# print(a.clear())
# print(a)

# set function part 3

print(a.union(e))
print(a)

print(b.difference(a))

print(b.difference_update(a))
print(b)
