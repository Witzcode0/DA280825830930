# https://docs.python.org/3/library/exceptions.html#bltin-exceptions

# print("start")
# print(a) # NameError: name 'a' is not defined
# print("end")

# print("start")
# a = int(input("Enter A"))
# b = int(input("Enter B")) 
# print(a / b) # ZeroDivisionError: division by zero
# print("end")

# try, except, else, finally, assert, raise

# print("start")
# # print(a / b + c)
# try:
#     a = int(input("Enter A"))
#     b = int(input("Enter B")) 
#     print(a / b + c)
# except ZeroDivisionError:
#     print("You can not divide by zero.")
# except NameError:
#     print("Oops!, something not define.")
# except Exception as err:
#     print("Error: ", err)
# print("end")

# try:
#     bal = 1000
#     wb = int(input("Enter a amount: "))

#     if wb <= bal:
#         print("Now remaining amount is : ", bal - wb)
#     else:
#         print("Inssufincent balance.")
# except Exception as e:
#     print("Error: ", e)

# try:
#     nums = [1,2]
#     print(nums[2])
# except IndexError:
#     print("element is not available in the list")
# except Exception as e:
#     print("Error: ", e)


# print("start")
# print(a / b + c)
# try:
#     a = int(input("Enter A"))
#     b = int(input("Enter B")) 
#     res = a / b
# except ZeroDivisionError:
#     print("You can not divide by zero.")
# except NameError:
#     print("Oops!, something not define.")
# except Exception as err:
#     print("Error: ", err)
# else:
#     print(res)
# print("end")

# try, except, else, finally, assert, raise

# print("start")
# try:
#     print(A)
# except Exception as e:
#     print(e)
# finally:
#     print("I will be always execute.")
# print("end")

bal = 1000
wb = int(input("Enter a amount: "))

# if wb <= bal:
#     print("Now remaining amount is : ", bal - wb)
# else:
#     print("Inssufincent balance.")

# assert (wb <= bal), "Inssufincent balance."


if wb > bal:
    raise ValueError("Inssufincent balance.")