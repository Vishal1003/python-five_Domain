# lmbda function
def fun(x): return x*x
print(fun(5))

print("---------------------")

# 2nd argument can be a collection (ds) and runs the first functiom in each item of that ds
length = map(len, ['vishal', 'honey', 'gaurav', 'subham'])
print(list(length))

print('----------------------')

# reduce function
from functools import reduce
total = reduce(lambda a, x: x + a, [0, 1, 2, 3, 4, 5])
print(total)

print('----------------------')

# filter function
arr = [1, 2, 3, 4, 5, 6]
for i in filter(lambda x: x > 5, arr):
    print(i)
