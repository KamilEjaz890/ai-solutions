"""
Problem #2
Date: 2026-07-10
Task: Write a Python implementation of K-Means clustering from scratch with a simple example.


import numpy as np

class KMeans:
    # Initialize KMeans class with number of clusters (k) and maximum iterations
    def __init__(self, k, max_iters=100):
        self.k = k
        self.max_iters = max_iters

    # Initialize centroids randomly
    def _init_centroids(self, X):
        # Choose k random points from the data as initial centroids
        indices = np.random.choice(X.shape[0], self.k, replace=False)
        self.centroids = X[indices, :]

    # Assign each data point to the closest centroid
    def _assign_clusters(self, X):
        # Calculate the distance between each data point and each centroid
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        # Assign each data point to the cluster with the closest centroid
        self.labels = np.argmin(distances, axis=1)

    # Update centroids as the mean of all data points in each cluster
    def _update_centroids(self, X):
        # Calculate the new centroid for each cluster
        for i in range(self.k):
            points_in_cluster = X[self.labels == i]
            if points_in_cluster.size:
                self.centroids[i] = points_in_cluster.mean(axis=0)

    # Main K-Means algorithm
    def fit(self, X):
        # Initialize centroids
        self._init_centroids(X)
        # Repeat the process until convergence or maximum iterations
        for _ in range(self.max_iters):
            # Assign clusters
            self._assign_clusters(X)
            # Store previous centroids
            prev_centroids = self.centroids.copy()
            # Update centroids
            self._update_centroids(X)
            # Check for convergence
            if np.all(self.centroids == prev_centroids):
                break

    # Predict cluster labels for new data points
    def predict(self, X):
        # Assign each data point to the closest centroid
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        return np.argmin(distances, axis=1)


# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    X = np.vstack((np.random.normal(0, 0.5, size=(25, 2)), np.random.normal(1, 0.5, size=(25, 2))))

    # Create a KMeans instance with k=2 clusters
    kmeans = KMeans(k=2)

    # Run the K-Means algorithm
    kmeans.fit(X)

    # Print the cluster labels
    print("Cluster labels:")
    print(kmeans.labels)

    # Print the centroids
    print("Centroids:")
    print(kmeans.centroids)

    # Predict cluster labels for new data points
    new_points = np.array([[0.5, 0.5], [1.5, 1.5]])
    print("Predicted cluster labels for new points:")
    print(kmeans.predict(new_points))
