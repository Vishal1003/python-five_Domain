# POLYMORPHISM : Taking multiple forms (same methods differentiated by objects)

class Duck :
    def quack(self):
        print("Duck's voice")

    def feathers(self):
        print("It has white feathers")


class Person:
    def quack(self):
        print("The peron can imitate duck")
    
    def feathers(self):
        print("Person picks the feather")
    
    def name(self):
        print("Mark Twain")
    

# polymorphism
def in_forest(obj):
    obj.quack()
    obj.feathers()

donald = Duck()
vishal = Person()

print(in_forest(donald))
print("-----------------------------")
print(in_forest(vishal))

