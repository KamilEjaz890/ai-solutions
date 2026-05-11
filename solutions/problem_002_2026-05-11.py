"""
Problem #2
Date: 2026-05-11
Task: Write a Python implementation of K-Means clustering from scratch with a simple example.


import numpy as np

class KMeans:
    # Initialize the KMeans class with the number of clusters (K) and the maximum number of iterations
    def __init__(self, K, max_iterations=100):
        self.K = K
        self.max_iterations = max_iterations

    # Initialize the centroids randomly
    def initialize_centroids(self, X):
        # Choose K random points from the data as the initial centroids
        np.random.seed(0)  # For reproducibility
        indices = np.random.choice(X.shape[0], self.K, replace=False)
        self.centroids = X[indices, :]

    # Calculate the Euclidean distance between a point and the centroids
    def calculate_distance(self, point):
        # Calculate the Euclidean distance between the point and each centroid
        distances = np.linalg.norm(point - self.centroids, axis=1)
        return distances

    # Assign each point to the closest centroid
    def assign_clusters(self, X):
        # Initialize an array to store the cluster assignments
        self.cluster_assignments = np.zeros(X.shape[0])

        # Iterate over each point in the data
        for i, point in enumerate(X):
            # Calculate the distance between the point and each centroid
            distances = self.calculate_distance(point)

            # Assign the point to the cluster with the closest centroid
            self.cluster_assignments[i] = np.argmin(distances)

    # Update the centroids based on the cluster assignments
    def update_centroids(self, X):
        # Initialize new centroids
        new_centroids = np.zeros(self.centroids.shape)

        # Iterate over each cluster
        for i in range(self.K):
            # Get the points assigned to the current cluster
            cluster_points = X[self.cluster_assignments == i]

            # If there are points in the cluster, update the centroid
            if cluster_points.shape[0] > 0:
                new_centroids[i] = np.mean(cluster_points, axis=0)

        # Update the centroids
        self.centroids = new_centroids

    # Run the K-Means algorithm
    def fit(self, X):
        # Initialize the centroids
        self.initialize_centroids(X)

        # Iterate over the maximum number of iterations
        for _ in range(self.max_iterations):
            # Assign each point to the closest centroid
            self.assign_clusters(X)

            # Update the centroids based on the cluster assignments
            previous_centroids = self.centroids.copy()
            self.update_centroids(X)

            # Check for convergence
            if np.all(self.centroids == previous_centroids):
                break

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    X = np.vstack((np.random.normal(0, 0.5, size=(25, 2)), np.random.normal(1, 0.5, size=(25, 2))))

    # Create a KMeans instance with K=2 clusters
    kmeans = KMeans(K=2)

    # Run the K-Means algorithm
    kmeans.fit(X)

    # Print the final centroids
    print("Final Centroids:")
    print(kmeans.centroids)

    # Print the cluster assignments
    print("\nCluster Assignments:")
    print(kmeans.cluster_assignments)
