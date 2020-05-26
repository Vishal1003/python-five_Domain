# Numpy is used more than list in scientific calculations. It has a 3D figure.

import numpy as np
import time
import sys

# List vs Numpy

# 1. Numpy takes less memory

# => List of 1000 size
print('=> SPACE COMPARISON')
S = range(1000)
print(sys.getsizeof(S)*len(S))

# => Numpy array of of 1000 size
D = np.arange(1000)
print(D.size*D.itemsize)


print('-------------------------------')

# 2. Numpy takes less time
print('=> TIME COMPARISON')
ex1 = range(10000)
ex2 = range(10000)

np1 = np.arange(10000)
np2 = np.arange(10000)

start = time.time()
result = [(x, y) for x, y in zip(ex1, ex2)]
print((time.time()-start)*1000)

start = time.time()
result = np1 + np2

print((time.time()-start)*1000)
