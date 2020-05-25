import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

customers = pd.read_csv('Ecommerce Customers')

#print(customers.info())
#print(customers.describe())

#sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=customers)

#sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=customers)

#sns.jointplot(x='Time on App', y='Length of Membership', kind='hex', data=customers)

#sns.pairplot(data=customers)

#sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=customers)

X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
Y = customers['Yearly Amount Spent']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=101)
lm = LinearRegression()
lm.fit(X_train, Y_train)
print(lm.coef_)
predictions = lm.predict(X_test)
#plt.scatter(Y_test, predictions)
#plt.xlabel('Y Test (True Values)')
#plt.ylabel('Predicted Values')
print('Mean Absolute Error : ', metrics.mean_absolute_error(Y_test, predictions))
print('Mean Squared Error : ', metrics.mean_squared_error(Y_test, predictions))
print('Root Mean Squared Error : ', np.sqrt(metrics.mean_squared_error(Y_test, predictions)))
print('Explained Variance Score : ', metrics.explained_variance_score(Y_test,predictions))

sns.distplot((Y_test-predictions), bins=50)

cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
print(cdf)

plt.show()