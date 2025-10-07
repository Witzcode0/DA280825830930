# name = "BMW"
# color = "orange"
# price = "20.5L"

# print(name)
# print(color)
# print(price)

# def run():
#     print("I can run")

# def horn():
#     print("pippppip")

# run()
# horn()

# syntax:

# class className:
#     block of code
    # data member 
    # member function


# class Car:
#     # data member [attributes and properties]
#     name = "BMW"
#     color = "orange"
#     price = "20.5L"

#     # member function [behaviour or method]
#     def run(yoyo):
#         print("I can run")

#     def horn(yoyo):
#         print("pippppip")

# # syntax of object

# # object_name = className()

# car1 = Car()
    
# print(car1.name)
# print(car1.color)
# print(car1.price)
# car1.run()
# car1.horn()


class Car:
    # Constructor
    def __init__(self, name, color, price):
        self.name_ = name
        self.color_ = color
        self.price_ = price
        print("i will auto call.")

    def carInfo(self):
        print("Car Information:")
        print("Name: ", self.name_)
        print("Color: ", self.color_)
        print("Price: ", self.price_)

while(True):
    name = input("Enter Name: ")
    color= input("Enter Color: ")
    price = input("Enter Price: ")
    obj = Car(name, color, price)
    obj.carInfo()

# c1 = Car("BMW", "red", "20L")
# c2 = Car("BMW", "orange", "20L")
# c3 = Car("BMW", "blue", "21L")

# print(c1.price_)
# print(c1.color_)
# print(c2.price_)
# print(c2.color_)

# c1.carInfo()
# c2.carInfo()
# c3.carInfo()