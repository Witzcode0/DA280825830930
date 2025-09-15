# What is function

# A function is a named, reusable block of code designed to perform a specific task. Functions are fundamental to writing organized, efficient, and maintainable code in Python.

# syntax:

# def function_name(para1, para2, ...paran): (parameter/arguments)
#     block of code

# function call
# function_name(val1, val2, ...valn)

# Types of function:
# 1] Built-in function
# 2] User-Define function


# s1 = 76 + 78 + 98 + 56 + 90
# print(s1/5)
# s2 = 76 + 67 + 99 + 56 + 90
# print(s2/5)

# def MarksAvg(s1, s2, s3, s4, s5):
#     total = s1 + s2 +s3 + s4 + s5
#     print(total/5)

# while(True):
#     subs = input("Enter a 5 sub marks sep by space: ").split(" ")
#     MarksAvg(int(subs[0]), int(subs[1]), int(subs[2]), int(subs[3]), int(subs[4]))


# Parameters types:
# 1] position para:

# def add(a, b, c):
#     print(a + b + c)

# add(10, 20, 30)

# 2] Variable length args:
# *args
# **kwargs

# nums = 10, 20, 30 # comma tuple
# print(type(nums))

# def add(*nums):
#     print(sum(nums))

# add(10, 20, 30, 40, 50, 60, 70, 80)

# 3] default/ keyword parameter:

# def bill(tomato, potato=50):
#     print(tomato + potato)

# bill(25, 100)

# def bill(**items):
#     # print(type(items))
#     total = 0
#     for key, value in items.items():
#         print(key, value)
#         total = total + value

#     print(total)
    

# bill(tomato=50, pen=100, book=200, milk=75)

# recursion, lambda, decorators, generator, global and local variable, function inside function