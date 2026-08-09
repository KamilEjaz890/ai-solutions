"""
Problem #2
Date: 2026-08-09
Task: Write a Python implementation of K-Means clustering from scratch with a simple example.


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    # Calculate the difference in x and y coordinates
    x_diff = point1[0] - point2[0]
    y_diff = point1[1] - point2[1]
    # Calculate the Euclidean distance using the Pythagorean theorem
    distance = np.sqrt(x_diff**2 + y_diff**2)
    return distance

# Define a function to initialize centroids randomly
def initialize_centroids(data, k):
    # Randomly select k data points as initial centroids
    indices = np.random.choice(len(data), k, replace=False)
    centroids = data[indices]
    return centroids

# Define a function to assign each data point to the closest centroid
def assign_clusters(data, centroids):
    # Initialize an empty list to store cluster assignments
    clusters = []
    # Iterate over each data point
    for point in data:
        # Initialize the minimum distance to infinity
        min_distance = float('inf')
        # Initialize the cluster assignment to None
        cluster = None
        # Iterate over each centroid
        for i, centroid in enumerate(centroids):
            # Calculate the distance between the point and the centroid
            distance = euclidean_distance(point, centroid)
            # If the distance is less than the minimum distance, update the minimum distance and cluster assignment
            if distance < min_distance:
                min_distance = distance
                cluster = i
        # Append the cluster assignment to the list
        clusters.append(cluster)
    return clusters

# Define a function to update centroids based on cluster assignments
def update_centroids(data, clusters, k):
    # Initialize an empty list to store updated centroids
    centroids = []
    # Iterate over each cluster
    for i in range(k):
        # Get the data points assigned to the current cluster
        cluster_points = [point for point, cluster in zip(data, clusters) if cluster == i]
        # Calculate the mean of the cluster points
        centroid = np.mean(cluster_points, axis=0)
        # Append the updated centroid to the list
        centroids.append(centroid)
    return centroids

# Define a function to perform K-Means clustering
def kmeans_clustering(data, k, max_iterations=100):
    # Initialize centroids randomly
    centroids = initialize_centroids(data, k)
    # Iterate over each iteration
    for _ in range(max_iterations):
        # Assign each data point to the closest centroid
        clusters = assign_clusters(data, centroids)
        # Update centroids based on cluster assignments
        new_centroids = update_centroids(data, clusters, k)
        # Check for convergence
        if np.all(centroids == new_centroids):
            break
        # Update centroids
        centroids = new_centroids
    return centroids, clusters

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    data = np.random.rand(100, 2)

    # Perform K-Means clustering with k=3
    k = 3
    centroids, clusters = kmeans_clustering(data, k)

    # Plot the clusters
    plt.scatter(data[:, 0], data[:, 1], c=clusters)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200)
    plt.show()
