# What is function

# A function is a named, reusable block of code designed to perform a specific task. Functions are fundamental to writing organized, efficient, and maintainable code in Python.

# syntax:

# def function_name(para1, para2, ...paran): (parameter/arguments)
#     block of code

# function call
# function_name(val1, val2, ...valn)

# Types of function:
# 1] Built-in function: print, type, id, len, sum, min, max, ord, chr
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

# recursion, 

# def squr(num):
#     print(num*num)

# squr(10)
# squr(5)

# Recursion in Python is a programming technique where a function calls itself to solve a problem. 

# fibbonaci

# 0 1 1 2 3 5 8 13.....

# n1 0 
# n2 1
# nth = n1 + n2 = 1

# def Fibbo(num):
#     n1 = 0
#     n2 = 1

#     if num > 2:
#         for i in range(1, num+1):
#             if i == 1:
#                 print(n1, end=" ")
#             elif i == 2:
#                 print(n2, end=" ")
#             else:
#                 nth = n1 + n2
#                 n1 = n2
#                 n2 = nth
#                 print(nth, end=" ")
#     else:
#         print("Invalid number")
# Fibbo(8)

# def test():
#     print("hi")

# str_ = test()
# print(str_)

# def test():
#     return "hi"

# str_ = test()
# print(str_, "brijesh")


# Factorial
# 5! = 5*4*3*2*1

# def fact(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * fact(num-1)
    
# print(fact(5))

# 

nums = [1,2,3,4,5,6,7,8,9,10]
# nums = 1

# s = lambda a, b, c: a + b + c
# print(s(10, 20, 30))

# def squr(num):
#     return num*num*num

# print(list(map(squr, nums)))
# print(tuple(map(lambda num: num * num * num, nums)))

# print(list(filter(lambda num: num % 2 == 0, nums)))
# print(list(filter(lambda num: num % 2 != 0, nums)))


# num = 10 # global

# def test():
#     num = 20  # local
#     print(num)

# test()
# print(num)


# num = 10 # global

# def test():
#     num = 20  # local
#     print(num)

# test()
# print(num)



# num = 10 # global

# def test():
#     global num 
#     num = 20
#     print(num)

# test()
# print(num)


# def outer():
#     print("I am a outer function")
#     def inner():
#         print("I am a inner function")
#     return inner()
# outer()


# generator
# def nums():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# num = list(iter(nums()))
# print(num)
# print(type(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))

# nums = [1,2,3,4]
# num = iter(nums)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))

# decorators

# def upperCase(yoyo):
#     def inner():
#         res = yoyo().upper()
#         print("Upper: ", res)
#         return res
#     return inner

# def swapCase(yoyo):
#     def inner():
#         res = yoyo().swapcase()
#         print("Swap: ", res)
#         return res
#     return inner

# @swapCase
# @upperCase
# def text():
#     return input("Enter a str: ")

# t = text()
# print(t)
