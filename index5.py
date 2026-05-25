import pandas as pd

data = {
    "Name": ["Ravi", "Aman", "Neha"],
    "Age": [22, None, 24],
    "Salary": [25000, 30000, None]
}

df = pd.DataFrame(data)

# Finding missing values
print(df.isnull())

# Count missing values
print(df.isnull().sum())

# Fill missing values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nUpdated DataFrame:")
print(df)