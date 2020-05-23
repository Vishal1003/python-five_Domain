# genrators are normal function with multiple return statements

def my_gen():
    n = 1
    print("this is the 1st ierator")
    yield n

    n += 1
    print("This is the second iterator")
    yield n


    n += 1
    print("This is the third iterator")
    yield n

func = my_gen()
print(next(func))
print(next(func))


print("----------------------")

# reversing the string
def rev_str(s):
    length = len(s)
    for i in range(length -1, -1, -1):
        yield s[i]


for char in rev_str("VISHAL"):
    print(char)


print("----------------------")

# generating expressions
my_li = [1, 3, 6, 10]

ans = (x**2 for x in my_li) 
print(next(ans))
print(next(ans))
print(next(ans))
