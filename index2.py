import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

df = pd.read_csv("SWP.csv")
X=df[['Year','Population']] 
Y=df['SolidWaste']
a=LinearRegression()
a.fit(X,Y)
year=int(input("enter the year: "))
population=int(input("enter the population: "))
s=a.predict([[year,population]])
print(s)
Y_pred = a.predict(X)
plt.scatter(df['Population'], df['SolidWaste'])
plt.plot(df['Population'], Y_pred)
plt.xlabel("Population")
plt.ylabel("Solid Waste")
plt.show()