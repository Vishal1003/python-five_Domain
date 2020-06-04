# DATA PREPROCESSING

#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing Dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,3].values

# Setting missing data
from sklearn.impute import SimpleImputer

missingvalues = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose = 0)
missingvalues = missingvalues.fit(X[:, 1:3])
X[:, 1:3]=missingvalues.transform(X[:, 1:3])

# Categorical Data

"""
This is done in order to ensure that all the data is in particular data type (integer).
Using dummy encoding 

"""

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float)

# Encoding Y data
from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y)


# Splitting the dataset into two parts (test and training):
from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""
test_set = 0.2 means 20% of the dataset is in test set and 80% in train set
"""

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)

"""
Do we need to fit and tranform dummy variables? 

It depends in the context. On tranforming the dummy variables the data interpretation 
looses. Though it doesnt break the data.

"""


    





