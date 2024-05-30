A = {"a":2,"c":23,"e":3,"r":22,"w":77}
# write a python program to sort a dictionary by value
A = sorted(A.values())
print(A)

# write a python progaram to print a dictionary where the keys are number between 1 and the value are squre of key
b = {}
for i in range(1,16):
    b[i]=i**2
print(b)

# write a program to multiply all the item a dictionary
product = 1
for i in b.values():
    product *= i
print(product)
# write a python program to sort a dictionary by key

p = {12:"a",2:"b",2:"c",3:"d"}

p = sorted(p.keys())
print(p)

