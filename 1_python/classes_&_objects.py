# python is not only the best scripting laguage but also supports oop paradigm.
# CLASS - It desctibes data and provides methods to manipulate that data, all ecompased in a single object


class Person:
    # attributes
    species = "HomeSapiens"

    # constructors
    def __init__(self, name, age, organization, height):
        self.name = name
        self.age = age
        self.organization = organization
        self.height = height

    def getInfo(self):
        print("I am {}. I'm currently working in {}. I'm {} yrs old and my height is {} cms".format(self.name, self.organization, self.age, self.height))

    def sleep(self):
        pass


per_son = Person("Vishal", 20, "NSUT", 180)
print(per_son.name)
print(per_son.age)
print(per_son.organization)

print("----------------")
print(per_son.getInfo())

print("----------------")



# Bound, Unbound and static methods

class A:

    @classmethod
    def f(self, x):
        print(2*x)

    @staticmethod
    def g(name):
        print("Hello {}!!!".format(name))

# # Creating class object and then calling =>
# a = A()
# a.g("Vishal")

# Auto instance calling =>
A.g('Vishal')
A.f(2)  # Don't bind anything