import csv
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("Housing (1).csv")
df=pd.DataFrame(data)
X = list(df.iloc[:, 1])
Y = list(df.iloc[:, 2])
plt.bar(Y, X, color='r',width=0.5)
plt.show()