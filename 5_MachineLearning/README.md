# MACHINE LEARNING 

## DATA PREPROCESSING :
Data prepocessing refers to manipulating the data to make it suitable for our model.
It includes following tasks :
1. Importing the dataset
2. Adding the missing values.
3. Encoding of some dats (if necessary) i.e Categorical Data.
4. Splitting the Dataset into the Training Set and Testing Set
5. Feature Scaling (if necessary)

`week1.py` includes all the above methods. While the template file includes omvly required methods that we will be using in upcomming sessions

## REGRESSION :
Regression models (both linear and non-linear) are used for predicting a real value, like salary for example. If your independent variable is time, then you are forecasting future values, otherwise your model is predicting present but unknown values. Regression technique vary from Linear Regression to SVR and Random Forests Regression.

Types :
1. Simple Linear Regression
2. Multiple Linear Regression
3. Polynomial Regression
4. Support Vector for Regression (SVR)
5. Decision Tree Classification
6. Random Forest Classification

### SIMPLE LINEAR REGRESSION

`y = b0 + b1*x1`

y : Dependent Variable
x : Independent Variable
b1 : slope 

     Salary Problem :
    `Salary = b0 + b1*Experience`

*BEST FITTING LINE* : `minimum of square(sum(y - y^))` (Ordinary Least Square Method)

Feature Scaling is to bring all the data in a particular scale. This will help to get accurate results. Feature Scaling in python is generally taken care on it's own though sometimes we need to explicitly do that. Feature Scaling can be done using standardization or normalization

          X(std) = (X - mean(X))/Standard Deviation(X)
          X(norm) = (X- min(X))/(max(X) - min(X))





