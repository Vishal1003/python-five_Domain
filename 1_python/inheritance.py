# Base Class
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

# Child Class (see area and perimeter are not in this class)
class Square(Rectangle):
    def __init__(self, s):
        super(Square, self).__init__(s, s)  #Super means the base class
        self.s = s


s = Square(5)
print('The are of the square is {} and perimeter is {}'.format(s.area(), s.perimeter()))


print("-----------------------------")

# Monkey Patching
# Adding some properties in the class without altering the original class

class A:
    def __init__(self, num):
        self.num = num
    
    def add(self, num2):
        return num2 + self.num

def get_num(self):
    return self.num

# MP
A.get_num = get_num

obj = A(42)
print(obj.get_num())

obj2 = A(22)
print(obj2.get_num())


