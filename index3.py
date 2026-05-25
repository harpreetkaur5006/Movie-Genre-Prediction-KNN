import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = []

for i in range(10):
    xi = int(input("Enter value for AGE[{i}]: "))
    yi = int(input("Enter value for AMOUNT[{i}]: "))
    X.append([xi, yi])

#print("Data points:", X)

k = int(input("Enter number of clusters: "))
kmeans = KMeans(k)
 kmeans.fit(X) 
# fit means training 


labels = kmeans.labels_  
centers = kmeans.cluster_centers_


cluster_names = []
for i in range(k):
    name = input("Enter name for Cluster {i}: ")
    cluster_names.append(name)

# Plot all points directly
plt.scatter([p[0] for p in X],
            [p[1] for p in X],
           c=labels,
            cmap='viridis')

# Plot centroids
plt.scatter(centers[:, 0], centers[:, 1],
            marker='X', s=200)

plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()


print("\nCluster Assignment:")
for i in range(len(X)):
    print(f"Point {X[i]} → {cluster_names[labels[i]]}")