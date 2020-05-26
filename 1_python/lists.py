list_a = [1, 4, 5, 10, 8, 9, 100]


# append
list_a.append(6)
# list_a.append([6, 7]) # list inside list

list_a.extend([6,7]) # appending two numbers at a time
list_a.remove(6)


list_a.reverse()
list_a.append(6)

# print(list_a.index(6)) 
# list_a.insert(0, 'vishal')
# print(list_a.count(6))

list_a.sort(reverse=True)

print(list_a[1:4])
print(len(list_a))

# chceking element presence
print(100 in list_a)