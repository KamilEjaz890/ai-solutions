"""
Problem #2
Date: 2026-06-10
Task: Write a Python implementation of K-Means clustering from scratch with a simple example.


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    # Calculate the difference in x and y coordinates
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    # Return the square root of the sum of the squares of the differences
    return np.sqrt(dx**2 + dy**2)

# Define a function to initialize centroids randomly
def initialize_centroids(data, k):
    # Choose k random points from the data as centroids
    indices = np.random.choice(len(data), k, replace=False)
    return data[indices]

# Define a function to assign each data point to the closest centroid
def assign_clusters(data, centroids):
    # Initialize an empty list to store the cluster assignments
    clusters = []
    # Iterate over each data point
    for point in data:
        # Initialize the minimum distance and the index of the closest centroid
        min_distance = float('inf')
        closest_centroid = -1
        # Iterate over each centroid
        for i, centroid in enumerate(centroids):
            # Calculate the distance between the point and the centroid
            distance = euclidean_distance(point, centroid)
            # If the distance is less than the minimum distance, update the minimum distance and the closest centroid
            if distance < min_distance:
                min_distance = distance
                closest_centroid = i
        # Append the index of the closest centroid to the list of cluster assignments
        clusters.append(closest_centroid)
    return np.array(clusters)

# Define a function to update the centroids based on the cluster assignments
def update_centroids(data, clusters, k):
    # Initialize an empty list to store the new centroids
    new_centroids = []
    # Iterate over each cluster
    for i in range(k):
        # Get the points assigned to the current cluster
        points_in_cluster = data[clusters == i]
        # If the cluster is not empty, calculate the new centroid as the mean of the points in the cluster
        if len(points_in_cluster) > 0:
            new_centroid = np.mean(points_in_cluster, axis=0)
        # If the cluster is empty, keep the old centroid
        else:
            new_centroid = np.random.rand(2)
        # Append the new centroid to the list of new centroids
        new_centroids.append(new_centroid)
    return np.array(new_centroids)

# Define a function to perform K-Means clustering
def kmeans_clustering(data, k, max_iterations=100):
    # Initialize the centroids randomly
    centroids = initialize_centroids(data, k)
    # Iterate over the maximum number of iterations
    for _ in range(max_iterations):
        # Assign each data point to the closest centroid
        clusters = assign_clusters(data, centroids)
        # Update the centroids based on the cluster assignments
        new_centroids = update_centroids(data, clusters, k)
        # If the centroids have not changed, stop the algorithm
        if np.all(centroids == new_centroids):
            break
        # Update the centroids
        centroids = new_centroids
    return clusters, centroids

# Define a simple example
if __name__ == "__main__":
    # Generate some random data
    np.random.seed(0)
    data = np.random.rand(100, 2)
    
    # Perform K-Means clustering with k=3
    k = 3
    clusters, centroids = kmeans_clustering(data, k)
    
    # Plot the data points and the centroids
    plt.scatter(data[:, 0], data[:, 1], c=clusters)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200)
    plt.show()
