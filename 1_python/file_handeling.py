try:
    with open('fname','r') as fp:
        for line in fp:
            print(line)

except FileExistsError:
    print("Abort!!! Error in this file")
