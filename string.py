name = "prit"
age = 23

a = "my name is {}.and age is {}"
print(a.format(name,age))

print(name.center(20,"*"))

# swap case
p = "   *****..... prit"

print(p.swapcase())

# strip
print(p.strip(" ,*,."))

# split

s = "oop#see#dpe"
print(s.split("#"))

# ljust

d = "Harry Poter"

print(d.ljust(20))

# rjust

l = "Harry Potter"

print(l.rjust(20,"&"))

# replace

v = "my name is prit"
print(v.replace("prit","chirag"))

