# In Python, a string is a sequence of characters, representing textual data.

# Indexing, Immutable

# Syntax:

# fristname = 'brijesh'
# fristname = "brijesh"
# fristname = """brijesh"""
# fristname = '''brijesh'''
# empty_str = str()
# empty_str = ''

company = "Bharat Futuris AI"

# left to right
# indexing(+/-) [object[postion]] : postion start by 0
# print(company[0])
# print(company[1])
# print(company[2])
# print(company[len(company)-1])

# print(company[-1])
# print(company[-10])

# Find the lenght of string
# print(len(company))

# right to left
#   +  -
# p 0 -6
# y 1 -5
# t 2 -4
# h 3 -3
# o 4 -2
# n 5 -1

# Slicing(+/-): object[start:end-1:step-1]

code = "python"
# print(code[1:3])
# print(code[2:5])
# print(code[::])
# print(code[:3])
# print(code[2:])
# print(code[::2])
# print(code[::3])

# print(code[::-1])
# print(code[-2:-5:-1][::-1])

# name = "nayan"
# print(name == name[::-1])

# code = "java"
# for ch in code:
#     print(ch)

fname = "brijesh"
lname = "gondaliya"

# concat
# fullname = fname + " " + lname
# print(fullname)

# replica
# print("*" * 5)

# string methods
company = "bhARaT FutURiSt aI"

# print(dir(company))
# 
# How to use object method
# syntax: object.method_name()

# print(company.lower())
# print(company.upper())
# print(company.title())
# print(company.capitalize())
# print(company.swapcase())

code = "pythtonTt"

# print(code.startswith("ph"))
# print(code.startswith("py"))
# print(code.endswith("on"))

# print(code.find("t"))
# print(code.find("t",3))
# print(code.find("t",5)) # garbge value
# print(code.find("T"))

# print(code.lower().count("t"))

# password = "123"

# print(password.isdigit())
# print(password.isalnum())
# print(password.isalpha())
# print(not password.isalnum())

# star = "*"

# # print(len(star))
# star2 = star.center(10,"_") 
# print(star2)
# print(len(star2))

# print(dir(code))

fullname = "     brijesh     gondaliya     "
# print(fullname.strip())
# print(fullname.lstrip())
# print(fullname.rstrip())
# print(fullname.strip().replace("  ", " ").replace("  ", " ").replace("  ", " "))

# print(fullname.strip().replace("  ", " ").replace("  ", " "))

# import re

# text = "   Hello   World \n   This   is   a   test   "
# cleaned = re.sub(r"\s+", " ", text).strip()
# print(cleaned)  # Output: Hello World This is a test

# name = "javascrip"
# book = 500

# print("my book name is python and it's price is 400")
# print("my book name is",name,"and it's price is",book)
# print(f"my book name is {name} and it's price is {book}")
# print("my book name is {} and it's price is {}".format(name, book))
# print("my book name is {1} and it's price is {0}".format(name, book))
# # print("my book name is %s and it's price is %d" % (name, book))

# print("my name is 'brijesh gondaliya'")
# print('my name is "brijesh gondaliya"')
# print("my name is \"brijesh gondaliya\"")

# print("\"")
# print("\\")
# print("\\\\")
# print("\'")

# print("brijesh go\\ndaliya")
# print(r"brijesh go\ndaliya")

# https://www.ascii-code.com/

num = 65
# print(chr(num))
# print(ord('A')) # return ascii value
# print(ord('a')) # return ascii value