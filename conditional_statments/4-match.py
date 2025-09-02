# match statments

# syntax: 

# match(exp):
#     case 1:
#         block of code
#     case 2:
#         block of code
#     case 3:
#         block of code
#     .....
#     case _:
#         block of code

# 0-mon, 1-tue......6-sun
# 1-mon, 2-tue......7-sun

import datetime

day = datetime.datetime.now().weekday()
print(day)

# day = 5
match(day):
    case 0:
        print("Today is Mon")
    case 1:
        print("Today is Tue")
    case 2:
        print("Today is Wed")
    case 3:
        print("Today is Thu")
    case 4:
        print("Today is Fri")
    case 5:
        print("Today is Sat")
    case 6:
        print("Today is Sun")
    case _:
        print("Invalid day")
