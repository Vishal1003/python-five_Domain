# LIST COMPREHENSIONS : Creates a new list by applying an expression to each element of an iterable.

# navie method
square = []
for x in (1, 2, 3, 4, 5):
    square.append(x*x)

print(square)

# LC method
sq_lc = [x*x for x in (1, 2, 3, 4, 5)]
print(sq_lc)

print("---------------------")

print([s.upper() for s in "Hello World !"])

print("---------------------")

# Conditional LC
print([x for x in range(10) if x % 2 == 0])

