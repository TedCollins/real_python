#This file runs a multivariate linear regression on simple test data in the form of arrays using scikit learn#
import numpy as np
from sklearn.linear_model import LinearRegression

#define arrays
x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

#fit model
model = LinearRegression().fit(x, y)

#print results
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"coefficients: {model.coef_}")

#predicted results
y_pred = model.predict(x)
print(f"predicted response:\n{y_pred}")