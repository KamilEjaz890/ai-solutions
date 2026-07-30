"""
Problem #2
Date: 2026-07-30
Task: Write a Python implementation of K-Means clustering from scratch with a simple example.


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    # Calculate the difference in x and y coordinates
    x_diff = point1[0] - point2[0]
    y_diff = point1[1] - point2[1]
    # Return the Euclidean distance
    return np.sqrt(x_diff**2 + y_diff**2)

# Define a function to initialize centroids randomly
def initialize_centroids(data, k):
    # Initialize centroids as random points from the data
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    return centroids

# Define a function to assign each data point to the closest centroid
def assign_clusters(data, centroids):
    # Initialize an array to store the cluster assignment for each data point
    cluster_assignments = np.zeros(data.shape[0])
    # Iterate over each data point
    for i, point in enumerate(data):
        # Initialize the minimum distance and the corresponding cluster
        min_distance = float('inf')
        cluster = -1
        # Iterate over each centroid
        for j, centroid in enumerate(centroids):
            # Calculate the distance between the point and the centroid
            distance = euclidean_distance(point, centroid)
            # Update the minimum distance and the corresponding cluster if necessary
            if distance < min_distance:
                min_distance = distance
                cluster = j
        # Assign the point to the closest centroid
        cluster_assignments[i] = cluster
    return cluster_assignments

# Define a function to update the centroids based on the cluster assignments
def update_centroids(data, cluster_assignments, k):
    # Initialize new centroids as the mean of each cluster
    new_centroids = np.zeros((k, data.shape[1]))
    # Iterate over each cluster
    for i in range(k):
        # Get the points assigned to the current cluster
        cluster_points = data[cluster_assignments == i]
        # Calculate the mean of the cluster points
        if cluster_points.size > 0:
            new_centroids[i] = np.mean(cluster_points, axis=0)
    return new_centroids

# Define a function to perform K-Means clustering
def kmeans_clustering(data, k, max_iterations=100):
    # Initialize centroids randomly
    centroids = initialize_centroids(data, k)
    # Iterate until convergence or max iterations
    for _ in range(max_iterations):
        # Assign each data point to the closest centroid
        cluster_assignments = assign_clusters(data, centroids)
        # Update the centroids based on the cluster assignments
        new_centroids = update_centroids(data, cluster_assignments, k)
        # Check for convergence
        if np.all(centroids == new_centroids):
            break
        # Update the centroids
        centroids = new_centroids
    return centroids, cluster_assignments

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    data = np.random.rand(100, 2)

    # Perform K-Means clustering
    k = 5
    centroids, cluster_assignments = kmeans_clustering(data, k)

    # Plot the clusters
    plt.scatter(data[:, 0], data[:, 1], c=cluster_assignments)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200)
    plt.show()
