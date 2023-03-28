import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv('Housing.csv')
df_binary = df[['area', 'price']]

 
#sns.lmplot(x ="area", y ="price", data = df_binary, order =4, ci = None)
import numpy as np
import numpy as np
X = np.array(df_binary['area']).reshape(-1, 1)
y = np.array(df_binary['price']).reshape(-1, 1)


import numpy as np

# Dropping any rows with Nan values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# Splitting the data into training and testing data
regr = LinearRegression()

regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))
y_pred = regr.predict(X_test)
plt.scatter(X_test, y_test, color ='b')
plt.plot(X_test, y_pred, color ='r')

plt.show()
# Data scatter of predicted values