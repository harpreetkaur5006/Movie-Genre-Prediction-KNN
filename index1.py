import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read existing file
df = pd.read_csv("HousePrices.csv")

# Create and train model
reg = LinearRegression()
reg.fit(df[['Area']], df['Price'])

# Predict price for Area = 3400
y = int(input("Enter Area: "))
predicted_price = reg.predict([[y]])[0]
print(predicted_price)

# Create new row with predicted value
new_row = pd.DataFrame({
    'Area': [y],
    'Price': [predicted_price]
})

# Append to existing data
df = pd.concat([df, new_row], ignore_index=True)

# Save back to SAME file
df.to_csv("HousePrices.csv", index=False)

#print("Predicted price appended successfully!")