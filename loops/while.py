# infinite loop

# syntax:

# while (condition):
    # block of code

# flag = True

# while(flag):
#     print("Bharat Futurist AI")

# while(1):
#     age = int(input("Enter your age: "))

#     if(age >= 18):
#         weight = float(input("Enter your weight: "))
#         if (weight >= 50):
#             print("You can donate")
#         else:
#             print("You can not donate")
#     else:
#         print("You can not donate")


# finite loop

# table = 5
# start = 1
# end = 10

# while(start <= end):
#     print(table, "*", start,"=" , table*start)
#     start = start + 1
    
# start 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# end = 10


start = 1
end = 10

while(start <= end):
    age = int(input("Enter your age: "))

    if(age >= 18):
        weight = float(input("Enter your weight: "))
        if (weight >= 50):
            print("You can donate")
        else:
            print("You can not donate")
    else:
        print("You can not donate")

    start = start + 1