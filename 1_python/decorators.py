# Decorators takes function as arguments, adds some functionalities and returns it 
# META Programming
# mainly used in web Development (changing many functionalities on user login)

def outer_fun(func):
    def inner():
        print("I got decorated")
        func()
    return inner

# method 1
@outer_fun
def ordinary():
    print("I'm ordinary")

ordinary()

# method 2 of calling
# ans_instance = outer_fun(ordinary)
# ans_instance()

print("------------------------")

# demo practical
def divide(func):
    def inner(a, b):
        print("I am going to divide {} by {}".format(a, b))
        if(b == 0):
            print("It is not possible to divide")
            return 
        return func(a, b)
    return inner

@divide
def smart_divide(a, b):
    print(a/b)

smart_divide(3, 2)


