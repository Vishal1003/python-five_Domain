arr = [1, 2, 3, 4, 5, 6]

my_itr = iter(arr)
print(next(my_itr)) # printint 1st element
print(next(my_itr)) # iterator here is on 2nd element

print(my_itr.__next__())
print(my_itr.__next__())


# Internal implementation of for loop in python
my_list = [1, 2, 3, 4, 5]
for element in my_list:
    pass

iter_obj = iter(my_list)

while True:
    try:
        element = next(iter_obj)
        pass
    except StopIteration:
        break




