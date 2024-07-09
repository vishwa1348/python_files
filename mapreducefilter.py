# map - map(function, iterator)

# def double(n):
#      return n*2


# my_list=[1,2,3,4,5,6,7,8]

# result=map(double,my_list)

# print(list(result))

# filter 

# def evenNumber(n):
#     return n%2==0

# my_list=[1,3,45,7,8,5,2,33,22,55,66,88]

# result=filter(evenNumber,my_list)

# print(list(result))


# reduce 

import functools


def product(x,y):
    return x*y

my_list=[1,2,3,4,5]

result=functools.reduce(product,my_list)

print(result)