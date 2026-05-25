import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import math

# Read dataset
df = pd.read_csv("MOVIE.csv")

# Features
X1 = df['IMDB'].tolist()
Y1 = df['DURATION'].tolist()

# Input new movie
X2 = float(input("Enter new movie IMDB rating: "))
Y2 = float(input("Enter duration for new movie: "))

# Distance function
def DISTANCE(X1, Y1, X2, Y2):
    dist = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    return dist

# Calculate distances
DIST2 = []

for i in range(len(X1)):
    dist = DISTANCE(X1[i], Y1[i], X2, Y2)
    DIST2.append(dist)

# Add distance column
df['Distance'] = DIST2

# Rank distances
df['RANK'] = df['Distance'].rank(method='min')

# Sort by distance
df_sorted = df.sort_values(by=['Distance'], ascending=True)

print(df_sorted)

# Value of K
k = int(input("Enter value for K: "))

# Prepare training data
X = df[['IMDB','DURATION']]
y = df['GENRE']

# Train model
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# Predict genre
predicted_genre = knn.predict([[X2, Y2]])

# Save sorted file
df_sorted.to_csv("MOVIES_sorted.csv", index=False)

print("\nTop K nearest movies:")
print(df_sorted[['RANK','MOVIE','IMDB','DURATION','GENRE','Distance']].head(k))

print("\nPredicted Genre:", predicted_genre[0])