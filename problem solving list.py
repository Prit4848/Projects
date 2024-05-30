A = ["Ross","Rachel","monica","joi"]

# write a program to swap first forth element
A[0],A[3]=A[3],A[0]
print(A)
# write a program to add new value to second position
A.insert(1,"prime")
print(A)

# write a program to delete a value of third position
B = [11,13,45,19]
B.pop(2)
print(B)

# write a program to multiply number in the list
a = [1,2,3,4,5]
mul = 1
for i in a:
    mul *= i
    print(mul)

# write a program to the get larger number from the list
a.sort()
print(a)
# write a program to get smaller number from list
print(a[0]) # first arange in acending order than use