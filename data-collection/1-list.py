# List - ordered, mutable, indexing, slicing, duplicate values are allowed

# syntax:

# list_name = list()
# list_name = []

# empty_list = []
# print(type(empty_list)) # <class 'list'>
# print(len(empty_list)) # 0

# nums = [1,2,3,4,5,5,5,3,2,6,45,43,3,6] 

# Access whole elements
# print(nums)

# indexing (+/-)
# print(nums[0])
# print(nums[-1])

# slicing (+/-)
# print(nums[:3])
# print(nums[2:])
# print(nums[::2])
# print(nums[::-1])


# mix_list = ["tomato", 50, 1.0]
# print(mix_list)

# nums = [1,2,3,4,5]
# nums[0] =  11 # using indexing
# nums[:2] = [11,22,33,44,55]
# print(nums)

nums = [1,2,3,4,5]
char = ['a','b','c','d','e']

# concat
# print(nums + char)

# replica 
# print(nums * 3)

# list methods
items = ["tomato", "potato", "pen", "book", "guava"]

# 

# print(dir(items))

# ADD
new_item_list = ["laptop", "desktop"]
# items.append(new_item_list)
# items.extend(new_item_list)
# items.insert(1, new_item_list)

# print(items.index("pen")) # return index of specific value

# DELETE

# items.pop() # by default remove last element from the list
# items.pop(2)
# items.remove("tomato")
# print(items)

print(items)
# items.clear()
# items.remove("tomato")
# print(items)

nums = [1,2,3,2,2,1,2,3,2,3,4,4,4]

# 'copy', 
# print(nums.count(4))
# nums.sort(reverse=True)
# nums.reverse()
# print(nums)

# copy_list = nums.copy()
# print(nums)
# print(copy_list)
# print(id(copy_list))
# print(id(nums))

# nested list
# items = [["tomato", 75, 1.5], ["Potato", 56, 2.0]]
# print(items[1][2])

nums = [1,2,3,4,5]
# print([num*num for num in nums]) # list compranhansive

new_list = []
for num in nums:
    new_list.append(num*num)
print(new_list)