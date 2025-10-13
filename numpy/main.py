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


# array attributes

arr = np.array([
    [1,2,3],
    [4,5,6]
])

# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.itemsize)
# print(arr.nbytes)
# print(arr.size * arr.itemsize)

arr1 = np.array([1,2,3,4,5, 6])
arr2 = np.array([11,22,33,44,55])
# print(arr + 2)
# print(arr * 2)

# print([1,2,3,4,5] + 3)

# print(arr1 + arr2)
# print(arr1 * arr2)


# arr = np.arange(1, 11, 1)
# arr = np.arange(1, 11, 2)
# arr = np.linspace(0, 1, 5)
# arr = np.linspace(0, 1, 10)

# arr = np.zeros((2, 5))

# arr = np.ones((2,3))
# arr = np.full((3, 3), 10)

# arr = np.random.rand(2,3) # 0 <= value < 1

# arr = np.eye(5)

# arr = np.random.randint(10, 20, (5, 2))

# print(arr)

# [_ _ _]
# [_ _ _]
# [_ _ _]

# arr = np.array([[1,2,3,4,5,6]])
new_arr = arr.flatten()

# new_arr = arr.reshape(2,3)
# arr = np.array([[1,2,3],[4,5,6]])

# print(dir(arr))
# print(arr.transpose())

a1 = np.array([1,2,3,4,5])
a2 = np.array([6,7,8,9,10])

# print(np.add(a1, a2))
# print(np.subtract(a1, a2))
# print(np.multiply(a1, a2))
# print(np.divide(a1, a2))
# print(np.dot(a1, a2))

# [1,2]  [5,6]
# [3,4]  [7,8] 

# m1 = np.array([[1,2],[3,4]])
# m2 = np.array([[5,6],[7,8]])
# print(np.dot(m1, m2))

# [[19 22]
#  [43 50]]
# arr = np.array([1,2,3,4,5])
# print(np.power(arr, 2))
# print(np.power(arr, 3))

# arr = np.array([1, 4, 9, 16, 25])
# print(np.sqrt(arr))

# arr = np.array([1,2,3,4,5])
# arr = np.array([1,2,4,5])
# arr = np.array([10, 15, 19])
# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))
# print(np.median(arr))

# arr = np.array([1,2,3,4,5])
# print(np.all(arr > 4))
# print(np.any(arr > 4))

