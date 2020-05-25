# Everything in python is object. 
# Class of class is called the meta class. 'type' is the super class in python

class VerboseMetaClass(type):
    # Overriding the new class
    def __new__(cls, class_name, class_parents, class_dict):
        print("Creating a new class named ", class_name)
        new_class = super().__new__(cls, class_name, class_parents, class_dict)
        return new_class

class Spam(metaclass = VerboseMetaClass):
    def info(self):
        print("Insert some elements")

s = Spam()
s.info()