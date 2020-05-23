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