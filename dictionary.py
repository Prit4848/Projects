# introduction to dictionary
Employee_Data = {"name":"john","age":24,"gender":"male"}
print(Employee_Data["age"])

# interation in dictionary
Student = {"Name":"joan","class":"5th","roll no":21}
# print(Student)
# for x in Student:
#     print(x)  # printing all key
#
# for x in Student:
#     print(Student[x])  # printing key value
#
# for x in Student.values():
#     print(x)  # printing key values
#
# for x,y in Student.items():
#     print(x,y)   # printing full dictionary
#
# # dictionary functions
# x = Student.get("Name")
# print(x)  # printing  name key values

# y = Student.items()
# print(y)  # full dictionary print
#
# z = Student.keys()
# print(z)   # printing all key
#
# a = Student.values()
# print(a) # print all key values
#
# d = Student.copy()
# print(d)  # use to copy the dictionary
#
# # dictionary iteration
#
b = Student.setdefault("pen no",220840116053)
print(b)
print(Student)
#
# c = Student.update("roll no ",22)
# print(c)

p = Student.pop("roll no")
print(p)
