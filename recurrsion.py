# recurrsion

# def recurrsion():
#     print("hello recurrsion called")
#     recurrsion()
# recurrsion()

# def recurrsion(n):


# recurrsion(10) 

# def m3():
#     m2()
#     print("m3 called")

# def m2():
#     m1()
#     print("m2 called")

# def m1():
#     print("m1 called")

# m3()


# def recurrsion(a):
#     if a!=0:
#         recurrsion(a-1)
#     print(a)

# recurrsion(10)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
