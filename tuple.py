
#change by index method
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

#add by append method
x = ("apple", "banana", "cherry")
y = list(x)
y.append("grapes")
x = tuple(y)
print(x)

# #we can remove also by remove method

# #unpack

# mytuple=("maths","english","tamil","science")
# m,*e,t=mytuple
# print(m)
# print(e)
# print(t)

# #loop
# mytuple=("maths","english","tamil","science")
# for i in range(len(mytuple)):
#     print(mytuple[i])

# #join two tuple
# mytuple=("maths","english","tamil","science")
# number=(1,2,3)
# print(mytuple+number)