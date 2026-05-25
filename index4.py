import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Waste_Management_and_Recycling_India.csv")

print(df.columns)

x = df[['Population Density (People/km²)']]
y = df['Waste Generated (Tons/Day)']

model = LinearRegression()
model.fit(x, y)

value = int(input("Enter Population Density: "))
prediction = model.predict([[value]])

print("Predicted Waste:", prediction[0])

