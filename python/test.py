import operator as op

# Strings in python
a = "Hello World"
print(a[0:5])
print(a[6:])  

print("--------SET---------")

# Set in python
py_set = set('abcde')
print(type(py_set))
print(py_set)

setT = {'banana', 'apple', 'orange'}
print(type(setT))

print("--------LISTS---------")
# LIST in python

list_a = [1, 2, 3, 4, "apple", "banana"]
print(list_a)
print(list_a[0: 2])


print("--------DICTONARY---------")
# DICTONARY in python

dict_a = {'name' : "John", 'age' : 25}
print(dict_a)

print(dict_a['name'])
print(dict_a.keys())
print(dict_a.values())

print("--------OPERATORS---------")
# OPERATORS in python
a, b, c, d = 3, 2, 2.5, -3
print(a/c)
print(a//c)

print(op.truediv(a,c))
print(op.floordiv(a,c))
