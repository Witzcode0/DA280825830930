# syntax:
# - key must be unique

dict_name = dict()
dict_name = {}

# dict_name = {
#     key1:value1,
#     key2:value2,
#     key3:value3,
#     ...
#     keyn:valuen,
# }

# print(type(dict_name))

user = {
    "first_name":"Brijesh",
    "last_name":"Gondaliya",
    "age":28,
}


# Access dictionary
# print(user)

# Access element of the dict
# print(user["first_name"])
# print(user["last_name"])
# print(user["age"])


# contacts = {
#     'A':[
#         {
#             'arjun':{
#                 'mobile':[7624756484,74658475684],
#                 'email': "arjun@gmail.com"

#             }
#         },{
#             'aman':{
#                 'mobile':[63547654736],
#                 'email':"aman@gmail.com"
#             }
#         }
#     ],
#     'B':[
#         {
#             'bubbun':{
#                 'mobile':[784687654, 7678568346]
#             }
#         },{
#             'bunty':{
#                 'mobile':[38478765847],
#                 'email':'bunty@gmail.com'
#             }
#         }
#     ]
# }

# print(contacts['B'])
# print(contacts['B'][1])
# print(contacts['B'][1]['bunty'])
# print(contacts['B'][1]['bunty']['mobile'])
# print(contacts['B'][1]['bunty']['mobile'][0])

d1 = {
    "key1":"value1"
}
d2 = {
    "key2":"value2"
}


# d3 = d1 + d2 # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# print(d3)

# print(d1 * 2) # TypeError: unsupported operand type(s) for *: 'dict' and 'int'

# Dict methods
# print(dir({}))


# car = {
#     "name":"BMW",
#     "model":"xyz",
#     "color":"red",
#     "price":"20L"
# }
# car.clear()
# copy_car = car.copy()
# print(copy_car)

# car.pop("price")
# car.popitem()
# print(car)




vegs = {
    "tomato": 50,
    "potato": 28,
    "apple":  150,
    "orange": 50
}

# print(vegs.get("potato")) # value
print(vegs.get("Guava")) # None

# print(vegs.keys())
# print(len(vegs.keys()))
# print(vegs.values())

# print(vegs.items())

# [
#     ('tomato', 50), 
#     ('potato', 28), 
#     ('apple', 150), 
#     ('orange', 50)
# ]

# for key,value in vegs.items():
#     print(key, value)



# n = None
# print(type(n))

#  'setdefault', 'update',

# fruites = ["apple", "banana", "guava", "orange"]
# qty = 10

# empty_dict = dict()

# print(empty_dict.fromkeys(fruites,qty))

# car = {
#     "name":"BMW",
#     "model":"xyz",
#     # "color":"red",
#     "price":"20L"
# }

# car.setdefault("color", "black")
# print(car)


d1 = {
    "key1":"value1"
}
d2 = {
    "key2":"value2",
    "key3":"value3"
}

d1.update(d2)
print(d1)
