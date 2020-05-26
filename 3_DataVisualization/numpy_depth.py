import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])

# Standard Dev
print(np.std(a))

print("-----------------------")

# Square root
print(np.sqrt(a))

print("-----------------------")

b = np.array([(7, 8, 9), (10, 11, 12)])
# Addition of arrays
print(a+b)

print("-----------------------")

# Attaching two arrays vertically
print(np.vstack((a,b)))

print("-----------------------")

# same but horizontally
print(np.hstack((a,b)))

print("-----------------------")

# Concatinating all rows in a single one
print(a.ravel())