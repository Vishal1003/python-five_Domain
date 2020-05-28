import pandas as pd

# Data Frame :
fruits = {
    'apples' : [3, 0, 1, 2],
    'oranges': [10, 5, 12, 7]
}

fruits = pd.DataFrame(fruits, index = ['Jan', 'Feb', 'Mar', 'Apr'])
print(fruits)

print("----------------------------------")

"""
Reading data from datafile
"""


