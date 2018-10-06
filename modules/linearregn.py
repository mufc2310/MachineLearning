import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("../../../Desktop/datasci-master/Final/Regression/Linear Regression/Salary_Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

plt.plot(X, y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

print('PREDICTED\t\tACTUAL')
for i in range(len(y_pred)):
    print(y_pred[i], '\t', y_test[i])

plt.scatter(X_train, y_train, color='red', label='Some1')
plt.plot(X_train, regressor.predict(X_train), color='blue', label='Some1')
plt.title('Salary vs. Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend(loc='upper left', numpoints=1)
plt.show()

plt.scatter(X_test, y_test, color='cyan')
plt.plot(X_train, regressor.predict(X_train), color='magenta')
plt.title('Salary vs. Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

