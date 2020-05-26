# The built in collections provide several specialized, flexible collections types that are both high performance
# and provide alternatives to the genral collections types of list, dict, tuple and set

# The module also defines the abstract base classes describing different types of collections functionalities
# such as Mutable set and ItemsView

import collections

counts = collections.Counter([1, 2, 3, 3, 1, 2, 2, 2])
print(counts)   # returns a dictonary with cound of each element as value

print("-----------------------------------")

from collections import deque

d = deque('Happy') # it will covert string to a list
for ele in d:
    print(ele.upper())


