# if elif ladder statments

# syntax:

# if(condition-1):
#     block of code
# elif (condition-2):
#     block of code
# elif (condition-3):
#     block of code
#     ...
# else:
#     block of code

score = 45

if (score >= 0) and (score <= 100):
    print("Valid score")
    if (score >= 80):
        print("Class A")
    elif (score >= 60):
        print("Class B")
    elif (score >= 40):
        print("Class C")
    else:
        print("Sorry, You are failed.")
else:
    print("Invalid score")


