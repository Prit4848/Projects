# write a program to find the max and min of in set
A = {12,33,5,546,42,22,5}
B = {1,2,3,4,5,6,7}
C = {2,4,5,6,8,10}
D = {3,4,5,6,7}
max = max(A)
min = min(A)
print("maximum:",max,"minimum:",min)

# write a program to find difference between two sets
print(A.difference(B))
# write a find common element in three list using set
a = A.intersection(B)
print(a.intersection(C))
# write an python program to remove an item from a set if is present in the set
print(A.discard(33))
print(A)
# write a python progarm to check if a set is subset of another set
print(D.issubset(B))
