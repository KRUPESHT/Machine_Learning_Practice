import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('KNN_Project_Data')
#print(df.head())

#sns.pairplot(data=df, hue='TARGET CLASS', plot_kws={'s': 5})
#sns.plt.show()

scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
X = df_feat
Y = df['TARGET CLASS']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=101)

#knn = KNeighborsClassifier(n_neighbors=1)
#knn.fit(X_train, Y_train)
#predictions = knn.predict(X_test)
#print(classification_report(Y_test, predictions))
#print(confusion_matrix(Y_test, predictions))

#error_rate = []
#for i in range(1, 60):
#    knn = KNeighborsClassifier(n_neighbors=i)
#    knn.fit(X_train, Y_train)
#    pred_i = knn.predict(X_test)
#    error_rate.append(np.mean(pred_i != Y_test))
#plt.figure(figsize=(10,6))
#plt.plot(range(1,60), error_rate, color='blue', linestyle='--', marker='o', markerfacecolor='red', markersize=10)
#plt.title('Error Rate vs K')
#plt.xlabel('K')
#plt.ylabel('Error Rate')
#plt.show()

#lowest error rate at k=31

knn = KNeighborsClassifier(n_neighbors=31)
knn.fit(X_train, Y_train)
predictions = knn.predict(X_test)
print(classification_report(Y_test, predictions))
print(confusion_matrix(Y_test, predictions))