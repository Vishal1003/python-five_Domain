# python operators work for the built in classes. But the same operator behaves diffrently with different data types.
# + operator is used for arithmatic addition of two num, merge two lists, concatinate two strings

# This feature in python, that allows same operator to have different meaning according to the context is called operator overloading

class A:
    def __init__(self, a):
        self.a = a
    
    def __add__(self, other):
        return self.a + other.a


obj1 = A(5)
obj2 = A(2)
print(obj1 + obj2) # add method is called automatically

print("------------------------------")

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        return self.a + other.a, self.b + other.b

vc1 = Vector(2, 4)
vc2 = Vector(1, 5)
print(vc1 + vc2)

print("------------------------------")

# Comparison Operator

class Op:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if(self.a < other.a):
            return "Obj1 is less than Obj2"
        else :
            return "Obj2 is less than Obj1"

obj1 = Op(15)
obj2 = Op(10)

print(obj1 < obj2)