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
