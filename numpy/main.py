import numpy as np

# nums = [1,2,3,4,5]
# arr = np.array(nums)

# print(arr)
# print(type(arr))

# print(np.__version__)

# 0D
arr = np.array(26)

# 1D
# arr = np.array([1,2,3,4,5])

# 2D
# matrix = [
#     [
#         1,2,3
#     ],
#     [
#         4,5,6
#     ]
# ]

# 3D

# matrix = [
#     [
#         [
#             1,2,3
#         ],[
#             4,5,6
#         ],[
#             7,8,9
#         ]
#     ]
# ]

# arr = np.array(matrix)
# print(arr.ndim)

# Access array indexing

# arr = np.array([1,2,3,4,5])
# print(arr[0])
# print(arr[0] + arr[-1])

# arr = np.array([[1,2,3, 11, 22, 33],[4,5,6, 44, 55, 66]])
# print(arr[0, 2])
# print(arr[1, 4])

# arr = np.array([
#     [
#         [1,2,3],[4,5,6]
#     ],[
#         [7,8,9], [10,11,12]
#     ]
# ])
# print(arr[1,1,1])


arr = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr[3:8])
# print(arr[3:])
# print(arr[:3])
# print(arr[-3:-1])

# print(arr[1:5:2])

arr = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

# print(arr[1, 0:3])
# print(arr[0, 2:5])
# print(arr[0:2, 2])
# print(arr[0:2, 1:4])


# Data types in numpy

# arr = np.array([1.2, 4.7, 34.89])
# arr = np.array(["laptop", "desktop", "plamtop", "pen"])
# print(arr.dtype)

# arr = np.array([1,2,3,4,5], dtype="S")
# arr = np.array([1,2,3,4,5], dtype="i4")
# arr = np.array(['a','b','c'], dtype="i")

arr = np.array([1.6, 32.78, 98.0])
# new_arr =arr.astype("i4")
# new_arr =arr.astype(int)
# new_arr =arr.astype(bool)
# print(new_arr.dtype)
