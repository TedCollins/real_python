#This script runs a multivariate regression and outputs the results with statsmod, which resembles R's summary functionality

#package imports
import numpy as np
import statsmodels.api as sm

#source data
x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

#add a constant to the ind variables in order for statsmodels to include a B0
x = sm.add_constant(x)

#fit a model :: note the backwards order
model = sm.OLS(y, x)

#calculate the results and print the summary
results = model.fit()
print(results.summary())

#pull out specific metrics from the regression results
print(f"coefficient of determination: {results.rsquared}")
print(f"adjusted coefficient of determination: {results.rsquared_adj}")
print(f"regression coefficients: {results.params}")

#predict results with the model
print(f"predicted response:\n{results.predict(x)}")
