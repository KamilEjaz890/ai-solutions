"""
Problem #2
Date: 2026-05-21
Task: Write a Python implementation of K-Means clustering from scratch with a simple example.


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a class for K-Means clustering
class KMeans:
    # Initialize the class with the number of clusters (K) and the maximum number of iterations
    def __init__(self, K, max_iters=100):
        self.K = K
        self.max_iters = max_iters

    # Initialize the centroids randomly
    def _init_centroids(self, X):
        # Choose K random points from the data as initial centroids
        indices = np.random.choice(X.shape[0], self.K, replace=False)
        self.centroids = X[indices, :]

    # Assign each data point to the closest centroid
    def _assign_clusters(self, X):
        # Calculate the distance between each data point and each centroid
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        # Assign each data point to the cluster with the closest centroid
        self.labels = np.argmin(distances, axis=1)

    # Update the centroids as the mean of all data points in each cluster
    def _update_centroids(self, X):
        # Update the centroids
        for i in range(self.K):
            points_in_cluster = X[self.labels == i]
            if points_in_cluster.size:
                self.centroids[i] = points_in_cluster.mean(axis=0)

    # Run the K-Means clustering algorithm
    def fit(self, X):
        # Initialize the centroids
        self._init_centroids(X)
        # Run the algorithm for the specified number of iterations
        for _ in range(self.max_iters):
            # Assign each data point to the closest centroid
            self._assign_clusters(X)
            # Update the centroids
            prev_centroids = self.centroids.copy()
            self._update_centroids(X)
            # Check for convergence
            if np.all(self.centroids == prev_centroids):
                break

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    X = np.vstack((np.random.normal(0, 0.5, size=(25, 2)), np.random.normal(1, 0.5, size=(25, 2))))

    # Create a K-Means clustering model with K=2
    model = KMeans(K=2)

    # Run the clustering algorithm
    model.fit(X)

    # Plot the clusters
    plt.scatter(X[:, 0], X[:, 1], c=model.labels)
    plt.scatter(model.centroids[:, 0], model.centroids[:, 1], c='red', marker='x', s=100)
    plt.show()
