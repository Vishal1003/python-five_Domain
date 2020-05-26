import numpy as np

# creating numpy array:

# Method 1:
np1 = np.arange(10000)

# Method 2:
np2 = np.array([(1, 2, 3)]) 


# Multidimentional:
arr = np.array([[(1, 2, 3)], [(4, 5, 6)], [(7, 8, 9)]])
print(arr.ndim)     # dimension

arr2 = np.zeros((2, 3, 2))
print(arr2.ndim)

print('------------------')

ar1 = np.array([(1, 2, 3, 4, 5, 6, 7, 8, 9)])

print(ar1.size)     # size of array
print(ar1.shape)    # row and col

print('------------------')

a = np.array([(8, 9, 10), (11, 12, 13)])
print(a)

print('------------------')

a = a.reshape(3, 2)
print(a)

print('------------------')

# SCLICING

a = np.array([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])

# ===> printing 2nd and 3rd element from 0th row
print(a[0,2:4])

# ===> printing 2nd element from each row (i.e 2nd col of 2D matrix)
print(a[0:,2])


print('------------------')

# linspace
# ==> For printing values in the range of x and y (np.linspace(x,y,no_of_values))
a = np.linspace(1, 4, 10)
print(a)

print('------------------')

# MAX/MIN or SUM

# 1D array
a = np.array([1, 2, 3, 4, 8, 15])
print("max in array: {}".format(a.max()))
print("min in array: {}".format(a.min()))
print("sum of array: {}".format(a.sum()))

# 2D array
a = np.array([(1, 2, 3), (4, 5, 6)])
print(a.sum(axis = 0))